'''
Link: https://www.lintcode.com/problem/clone-graph/description
'''

# I did not understand the question so I was unable to come up with my own solution.
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    def cloneGraph(self, node):
        root = node
        if node is None:
            return node
            
        # use bfs algorithm to traverse the graph and get all nodes.
        nodes = self.getNodes(node)
        
        # copy nodes, store the old->new mapping information in a hash map
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        
        # copy neighbors(edges)
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return mapping[root]
        
    def getNodes(self, node):
        q = collections.deque([node])
        result = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)
        return result
        
        

# Another solution from Jiuzhang.com. It says it is based on DFS and not recommended in interviews.
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
class Solution:

    def __init__(self):
        self.dict = {}
        
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if node is None:
            return None
            
        if node.label in self.dict:
            return self.dict[node.label]
            
        root = UndirectedGraphNode(node.label)
        self.dict[node.label] = root
        for item in node.neighbors:
            root.neighbors.append(self.cloneGraph(item))

        return root
    

# My own solution after doing it the second time after 17 days.
from collections import deque
class Solution:

    def __init__(self):
        self.dict = {}
        
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if node is None:
            return None
        # First create copies of the nodes, then set the neighbors attribute of them.
        queue = deque([node])
        visited = set([node])
        orig_node_to_copied_node = dict()
        while queue:
            this_node = queue.popleft()
            if this_node not in orig_node_to_copied_node:
                orig_node_to_copied_node[this_node] = UndirectedGraphNode(this_node.label)
            for nd in this_node.neighbors:
                if nd in visited:
                    continue
                queue.append(nd)
                visited.add(nd)
                
        head = orig_node_to_copied_node[node]
        for orig_node, copied_node in orig_node_to_copied_node.items():
            for nb in orig_node.neighbors:
                copied_node.neighbors.append(orig_node_to_copied_node[nb])
        return head
