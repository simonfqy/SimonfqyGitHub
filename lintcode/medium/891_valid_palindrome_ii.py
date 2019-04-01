'''
Link: https://www.lintcode.com/problem/valid-palindrome-ii/description
'''

# My own solution.
class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        # Write your code here
        
        left_removal_tried = False
        right_removal_tried = False
        left = left_recorded = 0
        right = right_recorded = len(s) - 1
        while left < right:
            # Determine whether it is palindromic
            if s[left] != s[right]:
                # Both tried and did not work.
                if left_removal_tried and right_removal_tried:
                    return False
                if not left_removal_tried:
                    # Remove the one pointed to by the left pointer.
                    left_recorded = left
                    right_recorded = right
                    left += 1
                    left_removal_tried = True
                    continue
                # Then left_removal_tried == True and right_removal_tried == False
                right_removal_tried = True
                left = left_recorded
                right = right_recorded
                right -= 1
                continue
            left += 1
            right -= 1
        return True
    
    
# This solution is based on the one given in Jiuzhang. Almost copying.
class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        # Write your code here
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
        if left >= right:
            return True
        return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)
    
    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
