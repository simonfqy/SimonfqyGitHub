"""
Link: https://www.lintcode.com/problem/k-closest-points/description
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

# My own solution. Uses heap.
import heapq

def less_than(self, other):
    diff = self.x ** 2 + self.y ** 2 - other.x ** 2 - other.y ** 2
    if diff != 0:
        return diff < 0
    if self.x != other.x:
        return self.x < other.x
    return self.y < other.y

Point.__lt__ = less_than

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        answer = []
        heap = []
        converted_to_orig = dict()
        for point in points:
            x_val = point.x - origin.x
            y_val = point.y - origin.y
            converted = Point(x_val, y_val)
            converted_to_orig[converted] = point
            heapq.heappush(heap, converted)
            
        while len(answer) < k:
            answer.append(converted_to_orig[heapq.heappop(heap)])
        return answer    
    
    
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
# The time complexity is O(nlogk).

import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        self.heap = []
        for point in points:
            dist = self.getDistance(point, origin)
            heapq.heappush(self.heap, (-dist, -point.x, -point.y))            
            if len(self.heap) > k:
                heapq.heappop(self.heap)

        ret = []
        while len(self.heap) > 0:
            _, x, y = heapq.heappop(self.heap)
            ret.append(Point(-x, -y))

        ret.reverse()
        return ret

    def getDistance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2    
    
    
 # My solution using a custom-implemented quick sort. Causes time limit exceeded problem.
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        point_to_squaresum = dict()
        self.sort(points, origin, 0, len(points) - 1, point_to_squaresum)
        return points[:k]
        
    def sort(self, points, origin, start, end, point_to_squaresum):
        left, right = start, end
        if right <= left:
            return
        pivot = points[(left + right) // 2]
        while left <= right:
            while left <= right and self.smaller_than(points, origin, points[left], pivot, \
                point_to_squaresum):
                left += 1
            while left <= right and self.smaller_than(points, origin, pivot, points[right], \
                point_to_squaresum):
                right -= 1
            if left <= right:
                points[left], points[right] = points[right], points[left]
                left += 1
                right -= 1
        self.sort(points, origin, start, right, point_to_squaresum)
        self.sort(points, origin, left, end, point_to_squaresum)
                
    def smaller_than(self, points, origin, point_one, point_two, point_to_squaresum):
        if point_one not in point_to_squaresum:
            squaresum_one = ((point_one.x - origin.x) ** 2) + ((point_one.y - origin.y) ** 2)
            point_to_squaresum[point_one] = squaresum_one
        else:
            squaresum_one = point_to_squaresum[point_one]
            
        if point_two not in point_to_squaresum:
            squaresum_two = ((point_two.x - origin.x) ** 2) + ((point_two.y - origin.y) ** 2)
            point_to_squaresum[point_two] = squaresum_two
        else:
            squaresum_two = point_to_squaresum[point_two]
            
        if squaresum_one != squaresum_two:
            return squaresum_one < squaresum_two
        if point_one.x != point_two.x:
            return point_one.x < point_two.x
        return point_one.y < point_two.y
    
    
# My own solution which uses heap. Has O(nlogn) time complexity.
import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        distance_heap = []
        results = []
        for point in points:
            distance = self.get_distance(point, origin)
            triplet = tuple([distance, point.x, point.y])
            heapq.heappush(distance_heap, triplet)
        for _ in range(k):
            _, x, y = heapq.heappop(distance_heap)
            results.append(Point(x, y))
        return results
        
    def get_distance(self, point_1, point_2):
        return ((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2) ** 0.5
    
    
