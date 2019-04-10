'''
Link: https://www.lintcode.com/problem/shortest-path-in-undirected-graph/description
'''

# Uses bidirectional BFS. I closesly followed the teachings on Jiuzhang.com.
from collections import deque
class Solution:
    """
    @param graph: a list of Undirected graph node
    @param A: nodeA
    @param B: nodeB
    @return:  the length of the shortest path
    """
    def shortestPath(self, graph, A, B):
        # Write your code here
        length = 0
        if A == B:
            return length
        queue_a, queue_b = deque([A]), deque([B])
        a_visited, b_visited = set([A]), set([B])
        while len(queue_a) and len(queue_b):
            size_queue_a, size_queue_b = len(queue_a), len(queue_b)
            if size_queue_a > 0:
                length += 1
            for _ in range(size_queue_a):
                node = queue_a.popleft()
                for neib in node.neighbors:
                    if neib in a_visited:
                        continue
                    if neib in b_visited:
                        return length
                    queue_a.append(neib)
                    a_visited.add(neib)
            if size_queue_b > 0:
                length += 1
            for _ in range(size_queue_b):
                node = queue_b.popleft()
                for neib in node.neighbors:
                    if neib in b_visited:
                        continue
                    if neib in a_visited:
                        return length
                    queue_b.append(neib)
                    b_visited.add(neib)
        
        return -1
