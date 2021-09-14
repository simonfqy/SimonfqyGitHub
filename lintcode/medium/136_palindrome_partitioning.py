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
            
            
# My own dynamic programming solution, iterative. The time and memory costs are quite high, but passes.
class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        if s == "":
            return [[]]
        dp = dict()
        n = len(s)
        for i in range(n):
            dp[(i, i)] = [[s[i]]]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if (i, j) not in dp:
                    dp[(i, j)] = []
                i_to_j = s[i : j + 1]
                # We have to consider the case where s[i : j + 1] itself is a whole palindromic string,
                # which cannot be captured by k below.
                if i_to_j == i_to_j[::-1]:
                    dp[(i, j)].append([i_to_j])
                for k in range(i, j):
                    substr = s[k + 1 : j + 1]
                    if substr != substr[::-1]:
                        continue
                    for prev_pal in dp[(i, k)]:
                        dp[(i, j)].append(prev_pal + [substr])
        return dp[(0, n - 1)]
    
    
# This solution is from jiuzhang.com, it is similar to my solution above, but uses memoization effectively.
class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        n = len(s)
        self.results = []
        self.is_palindrome = [[False] * n for _ in range(n)]
        self.populate_palindrome_array(s, n)
        self.add_partitions(s, 0, n - 1, [])
        return self.results

    def populate_palindrome_array(self, s, n):
        for i in range(n):
            self.is_palindrome[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                self.is_palindrome[i][i + 1] = True

        # This order is important. If we start i from 1, it will cause issues, because
        # we won't let the interval (i, j) gradually expand. There will be missed values [k][m] between [i][j] if
        # we increase i from 1.
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                self.is_palindrome[i][j] = self.is_palindrome[i + 1][j - 1] and s[i] == s[j]
    
    def add_partitions(self, s, start, end, partitions_so_far):
        if start > end:
            self.results.append(partitions_so_far)
            return
        for j in range(start, end + 1):
            if not self.is_palindrome[start][j]:
                continue
            curr_word = s[start : j + 1]
            self.add_partitions(s, j + 1, end, partitions_so_far + [curr_word])
