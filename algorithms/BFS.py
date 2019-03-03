"""
All right is reserved by Jiuzhang.
Typical use cases of Breadth First Search: Traversal in graph, which can be further divided into (1) Level Order Traversal, (2) Connected
Component, (3) Topological Sorting; Shortest Path in Simple Graph.
在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，称为该图的一个拓扑排序（英语：Topological sorting）:

1. 每个顶点出现且只出现一次；
2. 若A在序列中排在B的前面，则在图中不存在从B到A的路径。
也可以定义为：拓扑排序是对有向无环图的顶点的一种排序，它使得如果存在一条从顶点A到顶点B的路径，那么在排序中B出现在A的后面。
一张图的拓扑序列可以有很多个，也可能没有。拓扑排序只需要找到其中一个序列，无需找到所有序列。

拓扑排序的算法是典型的宽度优先搜索算法，其大致流程如下：

统计所有点的入度，并初始化拓扑序列为空。
将所有入度为 0 的点，也就是那些没有任何依赖的点，放到宽度优先搜索的队列中
将队列中的点一个一个的释放出来，放到拓扑序列中，每次释放出某个点 A 的时候，就访问 A 的相邻点（所有A指向的点），并把这些点的入度减去 1。
如果发现某个点的入度被减去 1 之后变成了 0，则放入队列中。
直到队列为空时，算法结束，
"""
# BFS without level-order traversal
from collections import deque

queue = deque()
seen = set() 

seen.add(start)
queue.append(start)
while len(queue):
    head = queue.popleft()
    for neighbor in head.neighbors:
        if neighbor not in seen:
            seen.add(neighbor)
            queue.append(neighbor)

# BFS with level order traversal
from collections import deque

queue = deque()
seen = set()

seen.add(start)
queue.append(start)
while len(queue):
    size = len(queue)
    # You will do something here, otherwise level order traversal is not necessary.
    for _ in range(size):
        head = queue.popleft()
        for neighbor in head.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
                
# 使用两个队列的BFS。该方法并无特别优点，仅仅更能体现BFS分层的效果。
from collections import deque 

queue1, queue2 = deque(), deque()
seen = set()

seen.add(start)
queue1.append(start)
currentLevel = 0
while len(queue1):
    size = len(queue1)
    for _ in range(size):
        head = queue1.popleft()
        for neighbor in head.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue2.append(neighbor)
    queue1, queue2 = queue2, queue1
    queue2.clear()
    currentLevel += 1

# 使用Dummy Node进行BFS。用 dummy node 来做占位符。即，在队列中每一层节点的结尾，都放一个 null（or None in Python，nil in Ruby），
# 来表示这一层的遍历结束了。避免了使用size，加深嵌套层次。
from collections import deque

queue = deque()
seen = set()

seen.add(start)
queue.append(start)
queue.append(None)
currentLevel = 0
while len(queue) > 1:
    head = queue.popleft()
    if head == None:
        currentLevel += 1
        queue.append(None)
        continue
    for neighbor in head.neighbors:
        if neighbor not in seen:
            seen.add(neighbor)
            queue.append(neighbor)
    
    
# Bidirectional BFS
"""
双向宽度优先搜索 (Bidirectional BFS) 算法适用于如下的场景：

无向图
所有边的长度都为 1 或者长度都一样
同时给出了起点和终点
以上 3 个条件都满足的时候，可以使用双向宽度优先搜索来求出起点和终点的最短距离。
"""
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
