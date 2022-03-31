'''
Link: https://www.lintcode.com/problem/978/
'''

# My implementation of the solution from jiuzhang.com. Uses stack.
class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s: str) -> int:
        sign = 1
        curr_number = 0
        result = 0
        stack = []
        for char in s:
            if char.isspace():
                continue
            if char.isnumeric():
                curr_number = 10 * curr_number + int(char)
                continue
            if char == "+":
                result += curr_number * sign
                sign = 1
                curr_number = 0
            elif char == "-":
                result += curr_number * sign
                sign = -1
                curr_number = 0
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                curr_number = 0
                sign = 1
                result = 0
            elif char == ")":
                result += sign * curr_number                
                sign = 1
                result *= stack.pop() # stack.pop() is the sign before the parenthesis
                result += stack.pop() # stack.pop() now is the result calculated before the parenthesis
                curr_number = 0
        if curr_number != 0:
            result += curr_number * sign
        return result

