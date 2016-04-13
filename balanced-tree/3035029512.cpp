#include <stdio.h>
#include <assert.h>
#include <algorithm>

struct node
{
	int key;
	int height;
	node *left, *right;
	node(int k)
	{
		key = k;
		height = 1;
		left = right = 0;
	}
};

/* Implement this function and in_order first */
void pre_order(node* root)
{
	if(root == 0) return;
	/* write something here */
	printf("%d ", root->key);
	pre_order(root->left);
	pre_order(root->right);
}

void in_order(node* root)
{
	/* write something here */
	if (root == 0) return;
	in_order(root->left);
	printf("%d ", root->key);
	in_order(root->right);
}

int height(node* r)
{
	return r ? r->height : 0;
}

void update_height(node* root)
{
	if(root == 0) return;
	int hl = height(root->left), hr = height(root->right);
	root->height = std::max(hl, hr) + 1;
}

void right_rotate(node*& ref_root)
{
	node *a = ref_root, *b = ref_root->left;
	ref_root = b; // This will change ref_root in the outside
	a->left = b->right;
	b->right = a;
	update_height(ref_root->right);
	update_height(ref_root);
}

void left_rotate(node*& ref_root)
{
	/* write something here */
	node *c = ref_root, *d = ref_root->right;
	ref_root = d;
	c->right = d->left;
	d->left = c;
	update_height(ref_root->left);
	update_height(ref_root);
}
/* Implement this function and left_rotate last,
 * You will get full points
 */
void maintain(node*& ref_root)
{
	if(ref_root == 0) return;
	update_height(ref_root);
	if(height(ref_root->left) > height(ref_root->right) + 1)
	{
		node*& p = ref_root->left; // I am a bit confused here. Does it mean that p is identical to ref_root->left, sharing the same address and information?
		if( height(p->left) < height(p->right) )
			left_rotate(p); // This will change ref_root->left.
		right_rotate(ref_root); // This will change ref_root in the outside.
	}
	else if(height(ref_root->right) > height(ref_root->left) + 1)
	{
		/* write something here */
	    node*& q = ref_root->right;
	    if (height(q->right) < height(q->left))
	       right_rotate(q);
	    left_rotate(ref_root);	    
	}
}


/* Implement this function second
 * This function together with in_order will get 30 pts
 */
void insert_key(int key, node*& ref_root)
{
	if(ref_root == 0){
		ref_root = new node(key);
		return;
	}
	if(key < ref_root->key)
		insert_key(key, ref_root->left);/* write something here */
	else if(key > ref_root->key)
		insert_key(key, ref_root->right);/* write something here */
	maintain(ref_root);
	// If you do not apply maintain, you can still maintain a binary search tree but not AVL tree
}

/* Implement this function third
 * This function together with insert,in_order,pre_order will get 90 pts
 */
void delete_key(int key, node*& ref_root)
{
	if(key < ref_root->key)
		delete_key(key, ref_root->left);/* write something here */
	else if(key > ref_root->key)
		delete_key(key, ref_root->right);/* write something here */
	else
	{
		if(ref_root->left && ref_root->right)
		{
			/* write something here */
			node *m = ref_root->right;
			while(m->left != 0){
				m = m->left;
			}
			ref_root->key = m->key;
			delete_key(m->key, ref_root->right);
			delete m;
		}
		else
		{
			/* write something here */
			if(ref_root->left != 0) ref_root = ref_root->left;
			else if(ref_root->right != 0) ref_root = ref_root->right;
			else ref_root = NULL;			
		}
	}
	maintain(ref_root);
	// If you do not apply maintain, you can still maintain a binary search tree but not AVL tree
}

int main()
{
	node *root = 0;
	char op[10] = "";
	int k;
	while(true)
	{
		scanf("%s", op);
		if(op[0] == 'E') break;
		switch(op[0])
		{
		case 'A': scanf("%d", &k); insert_key(k, root); break;
		case 'D': scanf("%d", &k); delete_key(k, root); break;
		case 'P': pre_order(root); printf("\n"); break;
		case 'I': in_order(root); printf("\n"); break;
		default: assert(0);
		}
	}
	return 0;
}
