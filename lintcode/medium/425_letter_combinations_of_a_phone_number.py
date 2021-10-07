'''
Link: https://www.lintcode.com/problem/425/
'''

# My own solution. Uses DFS, recursive.
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        results = []
        self.digit_to_letter = dict()
        self.digit_to_letter['2'] = ['a', 'b', 'c']
        self.digit_to_letter['3'] = ['d', 'e', 'f']
        self.digit_to_letter['4'] = ['g', 'h', 'i']
        self.digit_to_letter['5'] = ['j', 'k', 'l']
        self.digit_to_letter['6'] = ['m', 'n', 'o']
        self.digit_to_letter['7'] = ['p', 'q', 'r', 's']
        self.digit_to_letter['8'] = ['t', 'u', 'v']
        self.digit_to_letter['9'] = ['w', 'x', 'y', 'z']
        self.helper(digits, "", results)
        return results

    def helper(self, digits, combo_so_far, results):
        if digits == "":
            if combo_so_far != "":
                # This is to handle the special case where the input digits is "" and we want to return [] rather than [""].
                results.append(combo_so_far)
            return
        for char in self.digit_to_letter[digits[0]]:
            self.helper(digits[1:], combo_so_far + char, results)
            
# Iterative DFS solution, using stack.            
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if digits == "":
            return []
        results = []
        self.digit_to_letter = dict()
        self.digit_to_letter['2'] = ['a', 'b', 'c']
        self.digit_to_letter['3'] = ['d', 'e', 'f']
        self.digit_to_letter['4'] = ['g', 'h', 'i']
        self.digit_to_letter['5'] = ['j', 'k', 'l']
        self.digit_to_letter['6'] = ['m', 'n', 'o']
        self.digit_to_letter['7'] = ['p', 'q', 'r', 's']
        self.digit_to_letter['8'] = ['t', 'u', 'v']
        self.digit_to_letter['9'] = ['w', 'x', 'y', 'z']
        stack = [""]
        while stack:
            combo = stack.pop()
            if len(combo) == len(digits):
                results.append(combo)
                continue
            for char in self.digit_to_letter[digits[len(combo)]]:
                stack.append(combo + char)
        return results
    
    
# Using iterative BFS solution.            
from collections import deque
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # Have to handle this special case in the beginning.
        if digits == "":
            return []
        results = []
        self.digit_to_letter = dict()
        self.digit_to_letter['2'] = ['a', 'b', 'c']
        self.digit_to_letter['3'] = ['d', 'e', 'f']
        self.digit_to_letter['4'] = ['g', 'h', 'i']
        self.digit_to_letter['5'] = ['j', 'k', 'l']
        self.digit_to_letter['6'] = ['m', 'n', 'o']
        self.digit_to_letter['7'] = ['p', 'q', 'r', 's']
        self.digit_to_letter['8'] = ['t', 'u', 'v']
        self.digit_to_letter['9'] = ['w', 'x', 'y', 'z']
        queue = deque([""])
        curr_ind = 0
        while queue:
            if curr_ind == len(digits):
                return list(queue)
            # We're adding the characters corresponding to digits[curr_ind] in each iteration of the while loop.
            # So we must process all combinations ending in digits[curr_ind - 1] before incrementing the curr_ind.
            size = len(queue)
            for _ in range(size):
                combo = queue.popleft()            
                for char in self.digit_to_letter[digits[curr_ind]]:
                    queue.append(combo + char)
            curr_ind += 1
            
            
# The answer from a student on jiuzhang.com. It is iterative and uses 2 lists: temp and results, to store the temporary results
# when going through the digits.
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        results = []
        self.digit_to_letter = dict()
        self.digit_to_letter['2'] = ['a', 'b', 'c']
        self.digit_to_letter['3'] = ['d', 'e', 'f']
        self.digit_to_letter['4'] = ['g', 'h', 'i']
        self.digit_to_letter['5'] = ['j', 'k', 'l']
        self.digit_to_letter['6'] = ['m', 'n', 'o']
        self.digit_to_letter['7'] = ['p', 'q', 'r', 's']
        self.digit_to_letter['8'] = ['t', 'u', 'v']
        self.digit_to_letter['9'] = ['w', 'x', 'y', 'z']
        temp = [""]
        for digit in digits:
            results = []
            for letter in self.digit_to_letter[digit]:
                for prefix in temp:
                    results.append(prefix + letter)
            temp = results
        return results
