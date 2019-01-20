"""
All right is reserved by Jiuzhang.
Typical use cases of Breadth First Search: Traversal in graph, which can be further divided into (1) Level Order Traversal, (2) Connected
Component, (3) Topological Sorting; Shortest Path in Simple Graph.
在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，称为该图的一个拓扑排序（英语：Topological sorting）。

每个顶点出现且只出现一次；
若A在序列中排在B的前面，则在图中不存在从B到A的路径。
也可以定义为：拓扑排序是对有向无环图的顶点的一种排序，它使得如果存在一条从顶点A到顶点B的路径，那么在排序中B出现在A的后面。

拓扑排序的算法是典型的宽度优先搜索算法，其大致流程如下：

统计所有点的入度，并初始化拓扑序列为空。
将所有入度为 0 的点，也就是那些没有任何依赖的点，放到宽度优先搜索的队列中
将队列中的点一个一个的释放出来，放到拓扑序列中，每次释放出某个点 A 的时候，就访问 A 的相邻点（所有A指向的点），并把这些点的入度减去 1。
如果发现某个点的入度被减去 1 之后变成了 0，则放入队列中。
直到队列为空时，算法结束，
"""
# Bidirectional BFS
from collections import deque

def doubleBFS(start, end):
    if start == end:
        return 1

    # 2 queues, from the start and end, respectively.
    startQueue, endQueue = deque(), deque()
    startQueue.append(start)
    endQueue.append(end)
    step = 0

    # Sets of the visited vertices from the start and end
    startVisited, endVisited = set(), set()
    startVisited.add(start)
    endVisited.add(end)
    while len(startQueue) and len(endQueue):
        startSize, endSize = len(startQueue), len(endQueue)
        #　Level order traversal
        step += 1
        for _ in range(startSize):
            cur = startQueue.popleft()
            for neighbor in cur.neighbors:
                if neighbor in startVisited: # already visited nodes
                    continue
                elif neighbor in endVisited: # find overlap
                    return step
                else:
                    startVisited.add(neighbor)
                    startQueue.append(neighbor)
        step += 1
        for _ in range(endSize):
            cur = endQueue.popleft()
            for neighbor in cur.neighbors:
                if neighbor in endVisited:
                    continue
                elif neighbor in startVisited:
                    return step
                else:
                    endVisited.add(neighbor)
                    endQueue.append(neighbor)
    
    return -1
