'''
Link: https://www.lintcode.com/problem/178/
'''

from typing import (
    List,
)

# My implementation of the solution from jiuzhang.com. It takes advantage of the fact that a completely connected tree with n nodes 
# without cycles or duplicate edges should have n - 1 edges, and we should visit every node when doing BFS.
from collections import deque, defaultdict
class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if len(edges) != n - 1:
            return False
        node_to_neighbors = defaultdict(list)
        for node_1, node_2 in edges:
            node_to_neighbors[node_1].append(node_2)
            node_to_neighbors[node_2].append(node_1)
        queue = deque([0])
        visited = set([0])
        while queue:
            node = queue.popleft()
            for neighbor in node_to_neighbors[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        return len(visited) == n
      
      
# Solution from jiuzhang.com. Uses union find.
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        self.size = n
        self.father = {i: i for i in range(n)}
        for a, b in edges:
            self.union(a, b)
        return self.size == 1

    def union(self, a, b):
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a != root_b:
            # Merge the two subtrees together.
            self.size -= 1
            self.father[root_a] = root_b
            
    def find_root(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        # Overwrite the father of all the elements in the path to be the root.
        for n in path:
            self.father[n] = node
        return node
    
    
