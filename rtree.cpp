/* Implementations of R tree */
#include <cmath>
#include <algorithm>
#include <vector>
#include "rtree.h"
//Current task: to change the code based on new rtnode.h

const double EPSILON = 1E-10;

RTree::RTree(int entry_num)
{
	max_entry_num = entry_num;
	dimension = 2;//by default
	root = new RTNode(0, entry_num, NULL, NULL);
}

RTree::RTree(int entry_num, int dim)
{
	max_entry_num = entry_num;
	dimension = dim;//by default
	root = new RTNode(0, entry_num, NULL, NULL);
}

RTree::~RTree()
{
	delete root;
	root = NULL;
}


bool RTree::insert(const vector<int>& coordinate, int rid)
{
	if (coordinate.size() != this->dimension)
	{
		cerr << "R-tree dimensionality inconsistency\n";
	}

	//ADD YOUR CODE HERE
	//helper function for choosing leaf.
	RTNode* chooseLeaf(const RTNode& present, const BoundingBox& point){
		if (present.level == 0)
			return &present;
		int entryNum = present.entry_num;
		Entry* entries = present.entries;
		int enlargements[entryNum], area[entryNum];
		for (int i = 0; i < entryNum; i++){
			BoundingBox mbr = present.entries[i].get_mbr();
			enlargements[i] = mbr.enlargement(point);
			area[i] = mbr.get_area();
		}
		int minEnlarge = *min_element(enlargements, enlargements + entryNum);
		//occurrences stores the index where the enlargement equals the maximum.
		vector<int> occurrences;
		int index;
		for (int i = 0; i < entryNum; i++){
			if (enlargements[i] == minEnlarge)
				occurrences.push_back(i);
		}
		if(occurrences.size() == 1){
			//No ties. Go down a level.
			index = occurrences[0];
			chooseLeaf(*(entries[index].get_ptr()), point);
		}
		else{
			//Exist ties. First break ties with area.
			int dupNum = occurrences.size();
			//areaOfTiedElg stores the areas of tied smallest enlargements.
			vector<int> areaOfTiedElg;
			for (int i = 0; i < dupNum; i++){
				index = occurrences[i];
				areaOfTiedElg.push_back(area[index]);
			}
			int minArea = *min_element(areaOfTiedElg, areaOfTiedElg + dupNum);
			//tiedArea stores the index of tied entries after resolving by area.
			vector<int> tiedArea;
			for (int i = 0; i < dupNum; i++){
				if (areaOfTiedElg[i] == minArea)
					tiedArea.push_back(occurrences[i]);
			}
			if(tiedArea.size() == 1){
				//No ties remain after resolving through area.
				index = tiedArea[0];
				chooseLeaf(*(entries[index].get_ptr()), point);
			}
			else{
				//We have to resort to function tie_breaking to break the ties.
				int length = tiedArea.size();
				BoundingBox box1, box2; 					
				for (int i = 0; i < length - 1; i++){
					if (i ==0){
						box1 = entries[tiedArea[i]].get_mbr();
						index = tiedArea[i];
					}					
					box2 = entries[tiedArea[i+1]].get_mbr();
					if (tie_breaking(box1, box2)){
						box1 = box1;
						index = index;
					}
					else{
						box1 = box2;
						index = tiedArea[i+1];
					}
				}
				//Now the index to choose is determined.
				chooseLeaf(*(entries[index].get_ptr()), point);				
			}
		}		
	}
	
	//Node splitting function
	RTNode* splitNode(RTNode& node, const Entry& entry){
		//node is the node already full, entry is the new entry to be added.
		//We use a linear node splitting algorithm, which requires a linear pickSeed.
		//Subroutine linearPickSeeds returns two entries as the seeds of the two new nodes.
		Entry* linearPickSeeds(Entry* entries, int length){
			//length is the number of entries in the array.
			//dimension of bounding boxes.
			int dimension = entries[0].get_mbr().get_dim();
			//The following vector and two arrays has same length, which is "dimension".
			vector<double> separation;
			Entry* highestLows, lowestHighs;
			
			for (int j = 0; j < dimension; j++){
				//Do things along dimension j.
				//Entry highestLow, lowestHigh;
				int maximum, minimum, distance;
				//lows and highs store the lowest values and highest values in a dimension.
				vector<int> lows, highs;
				for (int i = 0; i < length; i++){
					//Now start filling vectors lows, highs. They both have "length" as their lengths.
					lows.push_back(entries[i].get_mbr().get_lowestValue_at(j));
					highs.push_back(entries[i].get_mbr().get_highestValue_at(j));				
				}
				int highestL, lowestH;
				//The following two are indices.
				int indHighestL, indLowestH;
				highestL = *max_element(lows, lows + length);
				lowestH = *min_element(highs, highs + length);
				//The following two vectors stores the indices of tied highest lows and lowest highs.
				vector<int> tiedHighestLow, tiedLowestHigh;
				for (int i = 0; i < length; i++){
					if(lows[i] == highestL)
						tiedHighestLow.push_back(i);
					if(highs[i] == lowestH)
						tiedLowestHigh.push_back(i);
				}
				if(tiedHighestLow.size() == 1){
					indHighestL = tiedHighestLow[0];
				}
				else{
					//There are tied highest lows, use tie_breaking to resolve the issue.
					BoundingBox box1, box2;
					int size = tiedHighestLow.size();
					int index; 					
					for (int i = 0; i < size - 1; i++){
						if (i == 0) {
							box1 = entries[tiedHighestLow[i]].get_mbr();
							index = tiedHighestLow[i];
						}					
						box2 = entries[tiedHighestLow[i+1]].get_mbr();
						if (tie_breaking(box1, box2)){
							box1 = box1;
							index = index;
						}
						else{
							box1 = box2;
							index = tiedHighestLow[i+1];
						}
					}
					//Now the variable index stores the index to be chosen as the Highest low.
					indHighestL = index;
				}
				if(tiedLowestHigh.size() == 1){
					indLowestH = tiedLowestHigh[0];
				}
				else{
					//There are tied highest lows, use tie_breaking to resolve the issue.
					int size = tiedLowestHigh.size();				
					for (int i = 0; i < size - 1; i++){
						if (i == 0) {
							box1 = entries[tiedLowestHigh[i]].get_mbr();
							index = tiedLowestHigh[i];
						}					
						box2 = entries[tiedLowestHigh[i+1]].get_mbr();
						if (tie_breaking(box1, box2)){
							box1 = box1;
							index = index;
						}
						else{
							box1 = box2;
							index = tiedLowestHigh[i+1];
						}
					}
					//Now the variable index stores the index to be chosen as the Highest low.
					indLowestH = index;
				}
				distance = highestL - lowestH;
				maximum = *max_element(highs, highs + length);
				mininum = *min_element(lows, lows + length);
				double separat = distance/(maximum - minimum);
				separation.push_back(separat);
				*highestLows = entries[indHighestL];
				*lowestHighs = entries[indLowestH];
				if (j != dimension - 1){
					highestLows++;
					lowestHighs++;
				}
			}
			//Now we have two arrays and a vector.
			double max_sep = *max_element(separation, separation + dimension);
			//Stores the ID of the dimension of tied maximum separation.
			vector<double> tiedMaxSep;
			for (j = 0; j < dimension; j++){
				if(separation[j] == max_sep){
					tiedMaxSep.push_back(j);
				}
			}
			//No matter there are ties or not, we always select tiedMaxSep[0].
			index = tiedMaxSep[0];
			Entry* outputs;
			outputs[0] = highestLows[index];
			outputs[1] = lowestHighs[index];
			//Proceed to check whether the two entries are duplicate.
			if(outputs[0] == outputs[1]){
				//We start sorting using tie_breaking function.
				Entry* candidates;
				for (i=0; i < length; i++){
					if (entries[i] != outputs[0]){
						*candidates = entries[i];
						if (i != length -1)
							candidates++;
					}
				}
				//candidates is actually an array with length "length - 1"
				//We don't need to sort all the elements in candidates. We just need to 
				//find the element box1 such that all tie_breaking(box1, x) returns False. 					
				for (int i = 0; i < length - 2; i++){
					if (i == 0) {
						box1 = candidates[i].get_mbr();
						index = i;
					}					
					box2 = candidates[i + 1].get_mbr();
					if (!tie_breaking(box1, box2)){
						box1 = box1;
						index = index;
					}
					else{
						box1 = box2;
						index = i+1;
					}
				}
				//Now "index" stores the index of the desired entry to be output.
				outputs[1] = candidates[index];			
			}
			return outputs;
		}
		
		//Subroutine pickNext
		void pickNext(RTNode* nodes, Entry & candidate ){
			RTNode* parents = nodes;
			//Choose by space utilization, avoid those which are already more than half full. 
			if(parents[0].entry_num > (parents[0].size)/2){
				//parents[0] is more than half full, any extra entries should go to parents[1].
				parents[1].entry_num++;
				parents[1].entries[parents[1].entry_num-1] = candidate;
				return;
			}
			else if (parents[1].entry_num > (parents[1].size)/2){
				parents[0].entry_num++;
				parents[0].entries[parents[0].entry_num-1] = candidate;
				return;
			}
			//Choose by least enlargement.
			//The following 2 variables correspond to MBRs of two groups.
			BoundingBox mbr0, mbr1;
			mbr0 = BoundingBox();
			mbr1 = BoundingBox();
			for (int i = 0; i < parents[0].entry_num; i++ ){
				mbr0.group_with(parents[0].entries[i].get_mbr());
			}
			for (i = 0; i < parents[1].entry_num; i++){
				mbr1.group_with(parents[1].entries[i].get_mbr());
			}
			int enlg0, enlg1;
			enlg0 = mbr0.enlargement(candidate.get_mbr());
			enlg1 = mbr1.enlargement(candidate.get_mbr());
			if(enlg0 < enlg1){
				parents[0].entry_num++;
				parents[0].entries[parents[0].entry_num-1] = candidate;
				return;
			}
			else if (enlg0 > enlg1){
				parents[1].entry_num++;
				parents[1].entries[parents[1].entry_num-1] = candidate;
				return;
			}
			//Tied. Choose by smallest area.
			if(mbr0.get_area() < mbr1.get_area()){
				parents[0].entry_num++;
				parents[0].entries[parents[0].entry_num-1] = candidate;
				return;
			}
			else if (mbr0.get_area() > mbr1.get_area()){
				parents[1].entry_num++;
				parents[1].entries[parents[1].entry_num-1] = candidate;
				return;
			}
			//Tied. Choose by number of entries.
			if(parents[0].entry_num < parents[1].entry_num){
				parents[0].entry_num++;
				parents[0].entries[parents[0].entry_num-1] = candidate;
				return;
			}
			else if (parents[0].entry_num > parents[1].entry_num){
				parents[1].entry_num++;
				parents[1].entries[parents[1].entry_num-1] = candidate;
				return;
			}
			//Tied. Choose by tie_breaking.
			if (tie_breaking(mbr0, mbr1)){
				parents[0].entry_num++;
				parents[0].entries[parents[0].entry_num-1] = candidate;
				return;
			}
			else{
				parents[1].entry_num++;
				parents[1].entries[parents[1].entry_num-1] = candidate;
				return;
			}				
		} 
		
		Entry ents [node.size + 1];
		for (int i = 0; i < node.size; i++){
			ents[i] = node.entries[i];
		}
		ents[node.size] = entry;
		Entry* seeds = linearPickSeeds(ents, node.size + 1);
		// seed[0] is the entry with the highest low side (in a certain dimension), seed[1]
		// is the entry with the lowest high side.
		// parents is a pointer (array) that is ultimately returned.
		RTNode* parents;
		parents[0] = RTNode(node.level, node.size, NULL, NULL);
		parents[1] = RTNode(node.level, node.size, NULL, NULL);
		parents[0].entries = &seeds[0]; parents[0].entry_num++;
		parents[1].entries = &seeds[1]; parents[1].entry_num++;
		
		Entry* cands;
		for(i = 0; i < node.size + 1; i++){
			if(ents[i] != seeds[0] && ents[i] != seeds[1]){
				*cands = ents[i];
				if(i != node.size )
					cands++;
			}
		}
		//cands is the pointer for all candidate entries to be put in RTNodes parents[0] and parents[1]
		for (i = 0; i < node.size - 1; i++){
			pickNext(parents, cands[i]);
		}
		
		return parents;		
	}
	
	//Helper function for adjusting trees after insertion.
	//Will return the pointers of the roots at the end.
	void adjustTree( RTNode *nodes , int size, int & rootCount, int rootLevel){
		RTNode* lowests = nodes;
		
		if (size == 1){
			//size == 1, only need to change the ancestor's bounding boxes.
			if (lowests[0].level == rootLevel){
				//Reached the root.
				return;
			}
			//Not reached the root, adjust covering rectangle in parent entry.
			Entry* pentry = lowests -> parent_entry;
			int entryNum = lowests -> entry_num;
			//Update the MBR of parent entry.
			for (int i = 0; i < entryNum; i++){
				(*pentry).get_mbr().group_with(lowests -> entries[i].get_mbr());
			}
			//Go up a level.
			adjustTree(lowests -> parent_node, size, rootCount, rootLevel);
		}
		else{
			//size == 2. Need to propagate splitting and change ancestor's MBR.
			if (lowests[0].level == rootLevel){
				//Reached the root.
				this -> root = lowests;
				rootCount++;
				return;
			}
			//adjust covering rectangle in each parent entry. Create a new parent entry for lowests[1].
			Entry p_entry1 = Entry(); // New parent of lowests[1]
			BoundingBox mbr1 = BoundingBox();
			int entryNum = lowests[1].entry_num;
			for (int i = 0; i < entryNum; i++){
				mbr1.group_with(lowests[1].entries[i].get_mbr());
			}
			p_entry1.set_mbr(mbr1);
			p_entry1.set_ptr(lowests[1]);
			lowests[1].parent_entry = &p_entry1;
			//Now change the parent entry of lowests[0].
			entryNum = lowests[0].entry_num;
			BoundingBox mbr0 = BoundingBox();
			for (i = 0; i < entryNum; i++){
				mbr0.group_with(lowests[0].entries[i].get_mbr());
			}
			lowests[0].parent_entry->set_mbr(mbr0);
			//Try inserting new entries into parent node.
			RTNode* p_node = lowests[0].parent_node;
			if (p_node->entry_num < p_node->size){
				(p_node->entry_num)++;
				p_node->entries[p_node->entry_num - 1] = p_entry1;
				lowests[1].parent_node = p_node;
				adjustTree(p_node, 1, rootCount, rootLevel);
			}
			else{
				//invoke splitNode to produce two new nodes.
				RTNode *newNodes = splitNode(*p_node, p_entry1);
				newNodes[0].parent_entry = p_node->parent_entry;
				newNodes[0].parent_entry->set_ptr(newNodes[0]);
				newNodes[0].parent_node = p_node->parent_node;
				adjustTree(newNodes, 2, rootCount, rootLevel);
			}
		}
	}
	
	BoundingBox point = BoundingBox(coordinate, coordinate);
	RTNode* present = this -> root;
	//We don't need to consider the case of inserting into an empty root, as it is included in the
	//general case.
	RTNode* leaf = chooseLeaf(*present, point);
	int rootCount = 1;
	int rootLevel = this -> root -> level;
	if (leaf -> entry_num < leaf -> size){
		//leaf node is not full yet. Could be inserted without splitting.
		(leaf -> entry_num)++;
		leaf -> entries[entry_num - 1] = Entry(point, rid);
		adjustTree(leaf, 1, rootCount, rootLevel);
	}
	else{
		//Splitting of leaf node is required.
		RTNode* newNodes = splitNode(*leaf, Entry(point, rid));
		newNodes[0].parent_entry = leaf->parent_entry;
		newNodes[0].parent_entry->set_ptr(newNodes[0]);
		//newNodes[1].parent_entry = leaf->parent_entry;
		newNodes[0].parent_node = leaf->parent_node;
		//newNodes[1].parent_node = leaf->parent_node;
		adjustTree(newNodes, 2, rootCount, rootLevel);
	}
	if (rootCount == 2){
		//Grow tree taller by creating a new root.
		rootLevel++;
		RTNode* newRoot = RTNode*();
	}
}

void RTree::query_range(const BoundingBox& mbr, int& result_count, int& node_travelled)
{
	if (mbr.get_dim() != this->dimension)
	{
		cerr << "R-tree dimensionality inconsistency\n";
	}

	//ADD YOUR CODE HERE
	/*Input: mbr, the query region represented by a bounding box.
	  Outputs: result_count, the number of points within the closed query range;
			   node_travelled, the number of nodes travelled in searching. */
	result_count = 0;
	node_travelled = 0;
	if (this -> root -> entry_num == 0){
		return;
	}
	RTNode* present = this -> root;
	DFS(mbr, result_count, node_travelled, *present);
	
	void DFS(BoundingBox mbr, int& result_count, int& node_travelled, const RTNode& present){
		node_travelled++;
		int entryNum = present.entry_num;
		Entry* ent = present.entries;
		int lev = present.level;
		for (int i = 0; i < entryNum; i++){
			// range is the MBR of entry i.
			BoundingBox range = ent[i].get_mbr();
			if (range.is_intersected(mbr)){
				if (lev == 0){
					result_count++;
				}
				else{
					DFS(mbr, result_count, node_travelled, *ent[i].get_ptr());
				}
			}
		}
	}
}


bool RTree::query_point(const vector<int>& coordinate, Entry& result)
{
	if (coordinate.size() != this->dimension)
	{
		cerr << "R-tree dimensionality inconsistency\n";
	}
    //ADD YOUR CODE HERE
	result = NULL;
    if (this -> root -> entry_num == 0){
		//The root is empty
		return false;
	}
	RTNode* present = this -> root;
	//Present is the node we are currently looking at.
	BoundingBox point = BoundingBox(coordinate, coordinate);
	return DFS(point, result, *present);
	
	bool DFS(BoundingBox point, Entry& result, const RTNode& present){		
		//entryNum is the number of valid entries in the current node.
		int entryNum = present.entry_num;
		Entry* ent = present.entries;
		//If lev = 0, the present RTNode is a leaf node.
		int lev = present.level;
		//found denotes whether the point has been found in lower leaves.
		bool found = false;
		for(int i = 0; i < entryNum; i++){
			//range is the MBR of entry i.
			BoundingBox range = ent[i].get_mbr();
			if(range.is_intersected(point)){
				//The point we are looking for is within the range of current bounding box.
				if (lev == 0){
					result = ent[i];
					return true;
				}
				else{
					//go down one more level.
					found = DFS( point, result, *ent[i].get_ptr());
					if (found)
						return true;
				}
			}
		}
		return found;
    }
 
            

}


/**********************************
 *
 * Please do not modify the codes below
 *
 **********************************/

//
// Calcuate the MBR of a set of entries, of size ``len''.
// Store the MBR in the first entry
//
BoundingBox RTree::get_mbr(Entry* entry_list, int len)
{
	BoundingBox mbr(entry_list[0].get_mbr());
	for (int i = 1; i < len; i++) {        
		mbr.group_with(entry_list[i].get_mbr());
	}
	return mbr;
}


/*********************************************************
  Return true means choose box1 for tie breaking.
  If the two boxes is the same, return true.
  This is to give a unified way of tie-breaking such that if your program is correct, then the result should be same, not influnced by any ties.
 *********************************************************/
bool RTree::tie_breaking(const BoundingBox& box1, const BoundingBox& box2)
{
	//for every dimension, try to break tie by the lowest value, then the highest
	for (int i = 0; i < box1.get_dim(); i++)
	{
		if (box1.get_lowestValue_at(i) != box2.get_lowestValue_at(i))
		{
			return box1.get_lowestValue_at(i) < box2.get_lowestValue_at(i);
		}
		else if (box1.get_highestValue_at(i) != box2.get_highestValue_at(i))
		{
			return box1.get_highestValue_at(i) > box2.get_highestValue_at(i);
		}
	}
	return true;
}


void RTree::stat(RTNode* node, int& record_cnt, int& node_cnt)
{
	if (node->level == 0) {
		record_cnt += node->entry_num;
		node_cnt++;
	}
	else {
		node_cnt++;
		for (int i = 0; i < node->entry_num; i++)
			stat((node->entries[i]).get_ptr(), record_cnt, node_cnt);
	}
}

void RTree::stat()
{
	int record_cnt = 0, node_cnt = 0;
	stat(root, record_cnt, node_cnt);
	cout << "Height of R-tree: " << root->level + 1 << endl;
	cout << "Number of nodes: " << node_cnt << endl;
	cout << "Number of records: " << record_cnt << endl;
	cout << "Dimension: " << dimension << endl;
}


void RTree::print_node(RTNode* node, int indent_level)
{
	BoundingBox mbr = get_mbr(node->entries, node->entry_num);

	char* indent = new char[4*indent_level+1];
	memset(indent, ' ', sizeof(char) * 4 * indent_level);
	indent[4*indent_level] = '\0';

	if (node->level == 0) {
		cout << indent << "Leaf node (level = " << node->level << ") mbr: (";
		for (int i = 0; i < mbr.get_dim(); i++)
		{
			cout << mbr.get_lowestValue_at(i) << " " << mbr.get_highestValue_at(i);
			if (i != mbr.get_dim() - 1)
			{
				cout << " ";
			}
		}
		cout << ")\n";
	}
	else {

		cout << indent << "Non leaf node (level = " << node->level << ") mbr: (";
		for (int i = 0; i < mbr.get_dim(); i++)
		{
			cout << mbr.get_lowestValue_at(i) << " " << mbr.get_highestValue_at(i);
			if (i != mbr.get_dim() - 1)
			{
				cout << " ";
			}
		}
		cout << ")\n";
	}

	Entry *copy = new Entry[node->entry_num];
	for (int i = 0; i < node->entry_num; i++) {
		copy[i] = node->entries[i];
	}

	for (int i = 0; i < node->entry_num; i++) {
		int index = 0; // pick next.
		for (int j = 1; j < node->entry_num - i; j++) {
			if (tie_breaking(copy[j].get_mbr(), copy[index].get_mbr())) {
				index = j;
			}
		}

		if (node->level == 0) {
			Entry& e = copy[index];
			cout << indent << "    Entry: <";
			for (int i = 0; i < e.get_mbr().get_dim(); i++)
			{
				cout << e.get_mbr().get_lowestValue_at(i) << ", ";
			}
			cout << e.get_rid() << ">\n";
		}
		else {
			print_node(copy[index].get_ptr(), indent_level+1);
		}
		// Move the output one to the rear.
		Entry tmp = copy[node->entry_num - i - 1];
		copy[node->entry_num - i - 1] = copy[index];
		copy[index] = tmp;

	}

	delete []indent;
	delete []copy;
}

void RTree::print_tree()
{
	if (root->entry_num == 0)
		cout << "The tree is empty now." << endl;
	else
		print_node(root, 0);
}
