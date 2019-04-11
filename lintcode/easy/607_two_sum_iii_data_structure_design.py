'''
Link: https://www.lintcode.com/problem/two-sum-iii-data-structure-design/description
'''

# My own solution, but partially referred to solutions from Jiuzhang.com
class TwoSum:
    
    def __init__(self):
        self.num_to_count = {}
        
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        if number not in self.num_to_count:
            self.num_to_count[number] = 0
        self.num_to_count[number] += 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        nums = list(self.num_to_count)
        for i in range(len(nums)):
            num1 = nums[i]
            if num1 * 2 == value:
                if self.num_to_count[num1] > 1:
                    return True
            elif value - num1 in self.num_to_count:
                return True
        return False

    
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        self.count = {}
        

    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        # Write your code here
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1
        

    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        # Write your code here
        for num in self.count:
            if value - num in self.count and \
                (value - num != num or self.count[num] > 1):
                return True
        return False
