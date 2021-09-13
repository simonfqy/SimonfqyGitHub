'''
Link: https://www.lintcode.com/problem/136/
'''

# My own solution, uses memoized DFS. I also verified that a DFS without memoization can still pass.
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
        # If we want to make "end" parameter also inclusive, simply change the below to range(start, end + 1)
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
    
    
# My own solution, uses DFS without memoization. A global variable stores all the lists of palindromes.
class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        self.palindromes = []
        self.get_palindromes(s, 0, len(s), [])
        return self.palindromes
    
    def get_palindromes(self, s, start, end, path_so_far):
        if start >= end:
            self.palindromes.append(path_so_far)
            return
        for i in range(start, end):
            first_substring = s[start : i + 1]
            if first_substring != first_substring[::-1]:
                continue
            # first_substring is a palindrome.
            self.get_palindromes(s, i + 1, end, path_so_far + [first_substring])   
