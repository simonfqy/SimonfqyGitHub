'''
Link: https://www.lintcode.com/problem/780/
'''

# My own solution. It is very slow, we need to use memoization to improve its performance. When we use prefixes in the recursive
# function parameters, we CANNOT use memoization, otherwise we'll have errors!
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        return self.get_longest_valid_strings(s, 0, "", 0)

    def get_longest_valid_strings(self, s, start, prefix, left_minus_right_count):
        if start >= len(s):
            if left_minus_right_count == 0:
                return [prefix]
            return [""]
        # NOTE: if we have prefix, we shouldn't use memoization, otherwise we'll have wrong answers. Remember it!
        # if start in self.memo:
        #     return self.memo[start]
        valid_strings = set()
        if s[start] == "(":
            valid_strings.update(self.get_longest_valid_strings(s, start + 1, prefix + s[start], left_minus_right_count + 1))
            valid_strings.update(self.get_longest_valid_strings(s, start + 1, prefix, left_minus_right_count))
        elif s[start] == ")":
            valid_strings.update(self.get_longest_valid_strings(s, start + 1, prefix, left_minus_right_count))
            if left_minus_right_count > 0:
                valid_strings.update(self.get_longest_valid_strings(s, start + 1, prefix + s[start], left_minus_right_count - 1))
        else:
            valid_strings.update(self.get_longest_valid_strings(s, start + 1, prefix + s[start], left_minus_right_count))
        if not valid_strings:            
            return [""]
        max_length = max([len(string) for string in valid_strings])
        longest_valid_strings = [string for string in valid_strings if len(string) == max_length]
        
        # self.memo[start] = longest_valid_strings
        return longest_valid_strings
    
    
# Also my own solution. Similar to the one above, but using global variables and the helper function doesn't return values, so it is
# traversal instead of divide-and-conquer. Time to execute is around 40% of the first solution, but still rather slow compared to other people's solutions.
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        self.valid_strings = set()
        self.max_length = 0
        self.helper(s, 0, "", 0)
        return [string for string in self.valid_strings if len(string) == self.max_length]

    def helper(self, s, pos, prefix, left_minus_right_count):
        if pos >= len(s):
            if left_minus_right_count == 0:
                if len(prefix) >= self.max_length:
                    self.valid_strings.add(prefix)
                    self.max_length = len(prefix)
                return
            self.valid_strings.add("")
            return
        if s[pos] == "(":
            self.helper(s, pos + 1, prefix + s[pos], left_minus_right_count + 1)
            self.helper(s, pos + 1, prefix, left_minus_right_count)
        elif s[pos] == ")":
            if left_minus_right_count > 0:
                self.helper(s, pos + 1, prefix + s[pos], left_minus_right_count - 1)
            self.helper(s, pos + 1, prefix, left_minus_right_count)
        else:
            self.helper(s, pos + 1, prefix + s[pos], left_minus_right_count)  
            
            
# A slightly optimized version of the one above. Takes ~45% less time to execute.             
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        self.valid_strings = set()
        self.max_length = 0
        self.helper(s, 0, "", 0)
        return [string for string in self.valid_strings if len(string) == self.max_length]

    def helper(self, s, pos, prefix, left_minus_right_count):
        if pos >= len(s) and left_minus_right_count == 0:
            if len(prefix) >= self.max_length:
                self.valid_strings.add(prefix)
                self.max_length = len(prefix)
            return            
        # Even if all of the remaining elements are ")", the left_minus_right_count will still > 0. So definitely this is not a valid string.
        if len(s) - pos < left_minus_right_count:
            self.valid_strings.add("")
            return
        if s[pos] == "(":
            self.helper(s, pos + 1, prefix + s[pos], left_minus_right_count + 1)
            self.helper(s, pos + 1, prefix, left_minus_right_count)
        elif s[pos] == ")":
            if left_minus_right_count > 0:
                self.helper(s, pos + 1, prefix + s[pos], left_minus_right_count - 1)
            self.helper(s, pos + 1, prefix, left_minus_right_count)
        else:
            self.helper(s, pos + 1, prefix + s[pos], left_minus_right_count)  
            
            
# Using BFS with 2 queues. Time to execute is about the same as the one above.
from collections import deque
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        max_length = 0 
        queue, queue_2 = deque([("", 0)]), deque([])
        valid_strings = set()

        for i in range(len(s)):
            while queue:
                prefix, left_minus_right_count = queue.popleft()
                if s[i] == "(":
                    # If s[i+1:] all being ")" will not make the left_minus_right_count equal to 0, prune.
                    if len(s) - i - 1 >= left_minus_right_count + 1:
                        queue_2.append((prefix + s[i], left_minus_right_count + 1))
                    queue_2.append((prefix, left_minus_right_count))
                elif s[i] == ")":
                    if left_minus_right_count > 0:
                        queue_2.append((prefix + s[i], left_minus_right_count - 1))
                    queue_2.append((prefix, left_minus_right_count))
                else:
                    queue_2.append((prefix + s[i], left_minus_right_count))
            queue, queue_2 = queue_2, queue
        while queue:
            string, left_minus_right_count = queue.popleft()
            if left_minus_right_count != 0 or len(string) < max_length:
                continue            
            valid_strings.add(string)
            max_length = len(string)
        return [string for string in valid_strings if len(string) == max_length]            
            
        
# Using BFS with 1 queue only. It is a slight variant of the one above. 
from collections import deque
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        max_length = 0 
        queue = deque([("", 0, -1)])
        valid_strings = set()
        
        while queue:
            prefix, left_minus_right_count, char_ind = queue.popleft()
            if char_ind == len(s) - 1:
                if left_minus_right_count == 0 and len(prefix) >= max_length:
                    valid_strings.add(prefix)
                    max_length = len(prefix)
                continue
            curr_ind = char_ind + 1
            if s[curr_ind] == "(":
                # If s[curr_ind + 1:] all being ")" will not make the left_minus_right_count equal to 0, prune.
                if len(s) - curr_ind - 1 >= left_minus_right_count + 1:
                    queue.append((prefix + s[curr_ind], left_minus_right_count + 1, curr_ind))
                queue.append((prefix, left_minus_right_count, curr_ind))
            elif s[curr_ind] == ")":
                if left_minus_right_count > 0:
                    queue.append((prefix + s[curr_ind], left_minus_right_count - 1, curr_ind))
                queue.append((prefix, left_minus_right_count, curr_ind))
            else:
                queue.append((prefix + s[curr_ind], left_minus_right_count, curr_ind))

        return [string for string in valid_strings if len(string) == max_length]
    
    
# Answer from jiuzhang.com provided by tutor. Uses some tricks and is highly specialized for this individual question, not very generic.
# The execution time is < 50% of the solution above, should be near optimal.
class Solution:
    def removeInvalidParentheses(self, s):
        res = []
        left, right = self._LeftRightCount(s)
        self._dfs(s, left, right, 0, res)
        return res       
            
    def _dfs(self, s, left, right, start, res):
        # Prune the branch; optimize the performance.
        if left < 0 or right < 0:
            return

        if left==0 and right==0:
            if self._isvalid(s):
                res.append(s)
            return
        
        for i in range(start, len(s)):
            # If the current s is not a valid string, and s[i] == s[i - 1], we can simply skip the
            # current i. That's because removing s[i] won't result in a valid string. If s[i] is not "(" or ")",
            # we shouldn't remove it. If it is "(" or ")", sooner or later we'll remove the characters in the "(" or ")" 
            # streak leading to s[i] starting from the beginning of the streak, in the two "if" statements below.
            if i > start and s[i] == s[i-1]:
                continue
            if s[i] == '(':
                # Try removing s[i] and see whether the new string is valid. The recursive function call
                # will also reset the starting index to i.
                self._dfs(s[:i]+s[i+1:], left-1, right, i, res)
            if s[i] == ')':
                self._dfs(s[:i]+s[i+1:], left, right-1, i, res)
    
    def _isvalid(self, s):
        left, right = self._LeftRightCount(s)
        return left==0 and right==0
    
    def _LeftRightCount(self, s):
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            if ch == ')':
                if left > 0:
                    left -= 1
                else:
                    # If we have more right parentheses than left ones at a certain point, the right counter will be increased, and can't be offset if we
                    # get left parentheses later.
                    right += 1
        return left, right    
    
    
# This solution doesn't work. Putting here to serve as a reminder, recording negative findings too.
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        return self.helper(s, 0, "", 0)

    def helper(self, s, start, prefix, left_minus_right_count):
        if start >= len(s):
            if left_minus_right_count == 0:
                return [prefix]
            return [""]
        valid_strings = set()
        for i in range(start, len(s)):
            if s[i] == "(":
                valid_strings.update(self.helper(s, i + 1, prefix + s[i], left_minus_right_count + 1))
            elif s[i] == ")":
                if left_minus_right_count == 0:                    
                    continue
                valid_strings.update(self.helper(s, i + 1, prefix + s[i], left_minus_right_count - 1))
            else:
                valid_strings.update(self.helper(s, i + 1, prefix + s[i], left_minus_right_count))
                
        max_len = max([len(string) for string in valid_strings])
        return [string for string in valid_strings if len(string) == max_len]
