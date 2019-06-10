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
