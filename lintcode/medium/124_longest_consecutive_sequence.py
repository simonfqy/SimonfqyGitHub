'''
Link: https://www.lintcode.com/problem/124/
'''

# My own solution. Has O(n) time complexity, picks arbitrary element from the num set and get the longest consecutive
# sequence the element is in. 
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        num_set = set(num)
        max_length = 0

        while num_set:
            curr_num = num_set.pop()
            current_length = 1
            start_num = curr_num - 1
            while start_num in num_set:
                num_set.remove(start_num)
                current_length += 1
                start_num -= 1
            start_num = curr_num + 1
            while start_num in num_set:
                num_set.remove(start_num)
                current_length += 1
                start_num += 1
            if current_length > max_length:
                max_length = current_length
        return max_length
    
    
# My own solution. Has O(nlogn) time complexity, uses the built-in sorted() function.
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        num = sorted(list(set(num)))
        max_length = 0
        prev = None
        curr_length = 1
        for number in num:
            if prev == number - 1:
                curr_length += 1
            else:
                curr_length = 1
            if curr_length > max_length:
                max_length = curr_length
            prev = number
        return max_length

