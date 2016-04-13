#include "boundingbox.h"


class RTNode;

class Entry {
private:
	BoundingBox mbr;
	RTNode* ptr;		//point to the node this entry represents, valid only if this is a non-leaf node entry.
	int rid;			// valid only if this is a leaf node entry.
	RTNode* parent_node;
	
public:
	Entry();
	Entry(const BoundingBox& thatMBR, const int rid);
	~Entry();
	const BoundingBox& get_mbr() const;
	RTNode* get_ptr() const;
	RTNode* get_parent() const;
	int get_rid() const;

	void set_mbr(const BoundingBox& thatMBR);
	void set_ptr(RTNode* ptr);
	void set_parent(RTNode* parent);

	void print();
};

class RTNode {
	public:
		RTNode(int lev, int size, Entry* pentry);        
		RTNode(const RTNode& other);
		RTNode& operator=(const RTNode& other);
		~RTNode();

	public:
		int entry_num;
		Entry* entries;
		int level;
		int size;	
		Entry* parent_entry;
};
