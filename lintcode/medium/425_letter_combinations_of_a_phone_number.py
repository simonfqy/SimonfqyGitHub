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
                results.append(combo_so_far)
            return
        for char in self.digit_to_letter[digits[0]]:
            self.helper(digits[1:], combo_so_far + char, results)
