"""
Depth First Search (DFS) can be either iterative or recursive. Recursive version is more straightforward, while iterative version is
often more efficient. The iterative version uses a stack to actively manage the order of nodes to be traversed.

Note that both of them need to have a variable to mark the visited nodes to avoid cycles.
"""

# Recursive
def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path
    
    
# Iterative
def dfs_iterative(graph, start):
    stack, path = [start], []
    
    # Use a stack to manage the order of the nodes.
    while stack:
        vertex = stack.pop()
        path.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor in path:
                continue
            stack.append(neighbor)

    return path
    
    
"""
The DFS of binary trees has 3 traversal orders: preorder, inorder and postorder. The recursive implementations are very easy to write 
and understand.
"""

# Recursive implementation
def printInorder(root):   
    if root: 
        printInorder(root.left) 
        print(root.val)
        printInorder(root.right)   
  
def printPostorder(root):   
    if root:   
        printPostorder(root.left) 
        printPostorder(root.right) 
        print(root.val)  
  
def printPreorder(root):   
    if root:   
        print(root.val)
        printPreorder(root.left) 
        printPreorder(root.right) 
        
        
# Iterative implementation of in-order traversal.
def printInorder(node):
    stack = []
    # Use the stack to manage traversal.
    while stack or node:
        if node: # this is a normal call, go to the left child. We want to get to the leftmost leaf.
            stack.append(node)
            node = node.left
        else: # If the current node is empty, get the higher-level node by popping the stack and returning its value.
            # Since we only append the nodes when the node is non-null, we are guaranteed to get meaningful values via
            # popping the stack. After popping the node, dive into its right subtree.
            node = stack.pop()
            print(node.value)
            node = node.right            
            
            
# Iterative implementation provided by jiuzhang.com      
def inorderTraversal(self, root):
    # write your code here
    inorder = []
    if root is None:
        return inorder

    dummy = TreeNode(0)
    dummy.right = root
    stack = [dummy]

    while stack:
        node = stack.pop()
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        if stack:
            inorder.append(stack[-1].val)

    return inorder
    
    
# Another iterative implementation in jiuzhang.com. It is more explicit and easier to understand compared to the solution above.
# It was used in 
# https://github.com/simonfqy/SimonfqyGitHub/blob/e8ae2c5a485cb63d456a03916f77c035d3cc58ed/lintcode/hard/86_binary_search_tree_iterator.py#L75
# and
# https://github.com/simonfqy/SimonfqyGitHub/blob/92b96e4cb25a9f1286aab35b03f127cae8a9529a/lintcode/hard/901_closest_binary_search_tree_value_ii.py#L149
def inorderTraversal(self, root):        
    inorder = []
    stack = []
    while root:
        stack.append(root)            
        root = root.left
    while stack:
        node = stack[-1]
        if node.right:
            n = node.right
            while n:
                stack.append(n)
                n = n.left
        else:
            n = stack.pop()                
            while stack and n == stack[-1].right:
                n = stack.pop()
        inorder.append(node.val)
    return inorder
    
 
# Iterative implementation of post-order traversal. It is a bit more complicated than in-order traversal. 
# Basic rationale: if we want to use a stack to pop the elements in a post-order traversal, we need to fill in the stack in the order
# or [root, right, left]. This is similar to the pre-order traversal of the tree, except that the left and right are switched. In light
# of this, we need to use two stacks, one for getting a pre-order traversal and pushing the nodes to the second stack, the second stack
# pops the elements in the order of post-order traversal.
def postOrderIterative(root):   
    if root is None: 
        return          
      
    # Create two stacks  
    s1 = [] 
    s2 = [] 
      
    # Push root to first stack 
    s1.append(root) 
      
    # Run while first stack is not empty 
    while s1:           
        # Pop an item from s1 and append it to s2 
        node = s1.pop() 
        s2.append(node)       
        # Push left and right children of removed item to s1 
        if node.left: 
            s1.append(node.left) 
        if node.right: 
            s1.append(node.right)   
        # Print all elements of second stack 
    while s2: 
        node = s2.pop() 
        print node.data

