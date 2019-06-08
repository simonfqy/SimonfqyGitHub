'''
Link: https://www.lintcode.com/problem/gray-code/description
'''
class Solution:
    """
    @param n: a number
    @return: Gray code
    """
    def grayCode(self, n):
        # write your code here
        # Use DFS.
        return self.get_gray_code(n, [0])
        
    def get_gray_code(self, n, gray_code_so_far):
        start_element = gray_code_so_far[-1]
        for i in range(n + 1):
            new_element = (1 << i) + start_element
            if new_element > 0 and new_element < 2**n and self.is_two_power(new_element ^ start_element) and \
                new_element not in set(gray_code_so_far):
                candidate_gray_code = self.get_gray_code(n, gray_code_so_far + [new_element])
                if len(candidate_gray_code) == 2**n:
                    return candidate_gray_code
        
            new_element = start_element - (1 << i)
            if new_element > 0 and new_element < 2**n and self.is_two_power(new_element ^ start_element) and \
                new_element not in set(gray_code_so_far):
                candidate_gray_code = self.get_gray_code(n, gray_code_so_far + [new_element])
                if len(candidate_gray_code) == 2**n:
                    return candidate_gray_code
        return gray_code_so_far                
            
    def is_two_power(self, number):
        count_one = 0
        while number != 0:
            if number & 1 == 1:
                count_one += 1
                if count_one > 1:
                    return False
            number = number >> 1
        return count_one == 1
    
    
# A more efficient solution, the new element can be determined prior to testing, saving some troubles.    
class Solution:
    """
    @param n: a number
    @return: Gray code
    """
    def grayCode(self, n):
        # write your code here
        # Use DFS.
        return self.get_gray_code(n, [0])
        
    def get_gray_code(self, n, gray_code_so_far):
        start_element = gray_code_so_far[-1]
        for i in range(n + 1):
            if (start_element >> i) & 1 == 0:
                new_element = (1 << i) + start_element
                if new_element > 0 and new_element < 2**n and \
                    new_element not in set(gray_code_so_far):
                    candidate_gray_code = self.get_gray_code(n, gray_code_so_far + [new_element])
                    if len(candidate_gray_code) == 2**n:
                        return candidate_gray_code
            else:
                new_element = start_element - (1 << i)
                if new_element > 0 and new_element < 2**n and \
                    new_element not in set(gray_code_so_far):
                    candidate_gray_code = self.get_gray_code(n, gray_code_so_far + [new_element])
                    if len(candidate_gray_code) == 2**n:
                        return candidate_gray_code
        return gray_code_so_far
