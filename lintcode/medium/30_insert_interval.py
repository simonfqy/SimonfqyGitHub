'''
Link: https://www.lintcode.com/problem/insert-interval/description
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# My own solution.
class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        new_left = newInterval.start
        new_right = newInterval.end
        if len(intervals) == 0:
            return [newInterval]
        new_intervals = []
        exist_modified_intervals = False
        new_interval_added = False
        for intvl in intervals:
            left = intvl.start
            right = intvl.end
            if left <= new_left and right >= new_right:
                return intervals
            if right < new_left:
                new_intervals.append(intvl)
                continue
            if left > new_right:
                if not exist_modified_intervals and not new_interval_added:
                    new_intervals.append(newInterval)
                new_intervals.append(intvl)
                new_interval_added = True
                continue
            if left <= new_left and right >= new_left and right < new_right:
                # create a new, larger interval.
                merged_intvl = Interval(left, new_right)
                new_intervals.append(merged_intvl)
                exist_modified_intervals = True
                continue
            if left >= new_left and right <= new_right:
                # Included in the new list.
                if exist_modified_intervals:
                    continue
                # Append new.
                new_intervals.append(newInterval)
                exist_modified_intervals = True
                continue
            if left <= new_right and right > new_right:
                if exist_modified_intervals:
                    new_intervals[-1].end = right
                    continue
                merged_intvl = Interval(new_left, right)
                new_intervals.append(merged_intvl)
                exist_modified_intervals = True
                continue
        if not new_interval_added and not exist_modified_intervals:
            new_intervals.append(newInterval)
        return new_intervals

    
# My solution based on the teachings from Jiuzhang.com.    
class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        new_left = newInterval.start
        new_right = newInterval.end
        if len(intervals) == 0:
            return [newInterval]
        new_intervals = []
        intervals_list = list(intervals)
        for i, intvl in enumerate(intervals):
            left = intvl.start
            if left < new_left:
                continue
            if left >= new_left:
                intervals_list.insert(i, newInterval)
                break
        if len(intervals_list) == len(intervals):
            intervals_list.append(newInterval)
        last = intervals_list[0].end
        for i, intvl in enumerate(intervals_list):
            if i == 0:
                new_intervals.append(intvl)
                continue
            this_left = intvl.start
            if this_left <= last:
                # Need to change the previous element.
                last_intvl = new_intervals[-1]
                last_intvl.end = max(intvl.end, last_intvl.end)
            else:
                new_intervals.append(intvl)
            last = new_intervals[-1].end
        return new_intervals
    
    
# This solution is from jiuzhang.com.    
class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        answer = []
        index = 0
        while index <= len(intervals) - 1 and intervals[index].start < newInterval.start:
            index += 1
        intervals.insert(index, newInterval)
        last = None
        for intvl in intervals:
            if last is not None and last.end >= intvl.start:
                last.end = max(last.end, intvl.end)
            else:
                last = intvl
                answer.append(last)
        
        return answer

    
# A clean and elegant solution. Only goes through the array once.    
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        results = []
        insertPos = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                results.append(interval)
                insertPos += 1
            elif interval.start > newInterval.end:
                results.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        results.insert(insertPos, newInterval)
        return results
