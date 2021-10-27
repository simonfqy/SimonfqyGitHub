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
    
    
# A solution from a student on jiuzhang.com. Has O(n) time complexity, the idea is similar to the solution above.
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        max_length = 0
        num_set = set(num)
        for number in num_set:
            if number - 1 in num_set:
                continue
            high = number + 1
            while high in num_set:
                high += 1
            max_length = max(max_length, high - number)
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

    
# A solution from a student on jiuzhang.com. Has O(n) time complexity, the special thing about it is that it only traverses 
# the num list once. However it is too tricky and not general enough.
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        max_length = 0
        number_to_streak_length = dict()
        nums_set = set(num)
        for number in num:
            if number in number_to_streak_length:
                continue
            left_length, right_length = 0, 0
            if number - 1 in number_to_streak_length:
                left_length = number_to_streak_length[number - 1]
            if number + 1 in number_to_streak_length:
                right_length = number_to_streak_length[number + 1]
            length = left_length + right_length + 1
            max_length = max(length, max_length)
            number_to_streak_length[number] = length
            number_to_streak_length[number - left_length] = length
            number_to_streak_length[number + right_length] = length

        return max_length

