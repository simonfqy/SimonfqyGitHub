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
