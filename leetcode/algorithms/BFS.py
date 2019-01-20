"""
All right is reserved by Jiuzhang.
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
