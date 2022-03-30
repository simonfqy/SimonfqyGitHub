'''
Link: https://www.lintcode.com/problem/1271/
'''

from typing import (
    List,
)

# Solution from a student on jiuzhang.com. 
class Solution:
    """
    @param n: the number of servers
    @param connections: connections
    @return: Critical Connections in a Network
    """
    def critical_connectionsina_network(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        node_to_neighbors = [[] for _ in range(n)]
        for node_a, node_b in connections:
            node_to_neighbors[node_a].append(node_b)
            node_to_neighbors[node_b].append(node_a)
        ranks = [float('-inf')] * n
        critical_connections = set()
        self.dfs_return_minimum_rank(0, -1, 0, ranks, critical_connections, node_to_neighbors)
        return list([list(connection) for connection in critical_connections])
    
    def dfs_return_minimum_rank(self, node, father, depth, ranks, critical_connections, node_to_neighbors):
        ranks[node] = depth
        for child in node_to_neighbors[node]:
            if child == father:
                continue
            if ranks[child] < 0:
                ranks[node] = min(ranks[node], self.dfs_return_minimum_rank(child, node, 
                        depth + 1, ranks, critical_connections, node_to_neighbors))
            else:
                ranks[node] = min(ranks[node], ranks[child])
        if node != 0 and ranks[node] == depth:
            critical_connections.add(tuple(sorted((father, node))))
        return ranks[node]

