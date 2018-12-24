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
        print(root.val), 
  
  
def printPreorder(root):   
    if root:   
        print(root.val)
        printPreorder(root.left) 
        printPreorder(root.right) 
        
# Iterative implementation
def printInorder(node):
    stack = []
    while stack and node:
        if node: # this is a normal call, recurse
            stack.append(node)
            node = node.left
        else: # we are now returning: pop and print the current node
            node = stack.pop()
            print(node.value)
            node = node.right
   

