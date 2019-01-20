"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        
        output_list = []
        node_to_indegree = {x: 0 for x in graph}
        for node in graph:
            neighbors = node.neighbors
            for nb in neighbors:
                node_to_indegree[nb] += 1
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = deque(start_nodes)
        while queue:
            node = queue.popleft()
            output_list.append(node)
            for nb in node.neighbors:
                node_to_indegree[nb] -= 1
                if node_to_indegree[nb] == 0:
                    queue.append(nb)
        
        return output_list
