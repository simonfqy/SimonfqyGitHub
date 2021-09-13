'''
Link: https://www.lintcode.com/problem/136/
'''

# My own solution, uses memoized DFS.
class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        self.memo = dict()
        return self.get_palindromes(s, 0, len(s))

    # start is inclusive, end is not.
    def get_palindromes(self, s, start, end):
        if start >= end:
            return [[]]
        if (start, end) in self.memo:
            return self.memo[(start, end)]
        palindromes = []
        for i in range(start, end):
            first_substring = s[start : i + 1]
            if first_substring != first_substring[::-1]:
                continue
            # first_substring is a palindrome.
            subsequent_palindrome_lists = self.get_palindromes(s, i + 1, end)
            for subsequent_palindromes in subsequent_palindrome_lists:
                palindromes.append([first_substring] + subsequent_palindromes)
        self.memo[(start, end)] = palindromes
        return palindromes
