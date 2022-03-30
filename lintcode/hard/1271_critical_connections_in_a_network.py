'''
Link: https://www.lintcode.com/problem/1271/
'''

from typing import (
    List,
)

# Solution from a student on jiuzhang.com. 整体的思路就是，把带环的删掉，剩下的就是关键链接。具体方法就是，
# 用dfs的层级来代表啥时候visit过，如果发现之前就visit过，那么说明有环，并且整个环的全部节点层级都设定为环上诸节点中最小的层级。
# 这样我们就可以通过某节点层级与其当前dfs深度的对比，得知该节点是否在环上。如果不在环上，将其加入result中。
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

