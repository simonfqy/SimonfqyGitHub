'''
Link: https://www.lintcode.com/problem/1283/
'''

# My own solution. Using two pointers.
class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverse_string(self, s: str) -> str:
        # write your code here
        left, right = 0, len(s) - 1
        # Using * is called unpacking.
        char_list = [*s]
        while left < right:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
        return ''.join(char_list)
      
      
