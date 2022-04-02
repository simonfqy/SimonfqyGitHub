'''
Link: https://www.lintcode.com/problem/849
'''

# My own solution. Uses stack.
class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        curr_num = 0
        sign = "+"
        for i, char in enumerate(s):
            if char.isnumeric():
                curr_num = curr_num * 10 + int(char)                
            if i == n - 1 or (not char.isspace() and not char.isnumeric()):
                if char == "(":
                    stack.append(sign)
                    sign = "+"
                elif char == ")":
                    self.reduce_stack_after_parentheses(stack, sign, curr_num)
                    sign = None
                else:
                    self.modify_stack(stack, sign, curr_num)     
                    sign = char
                curr_num = 0
         
        return sum(stack)
    
    def modify_stack(self, stack, sign, curr_num):
        if not sign:
            return
        if sign == "+":
            stack.append(curr_num)
        elif sign == "-":
            stack.append(-curr_num)
        elif sign == "*":
            stack.append(stack.pop() * curr_num)
        elif sign == "/":
            stack.append(int(stack.pop() / curr_num))

    def reduce_stack_after_parentheses(self, stack, sign, curr_num):
        self.modify_stack(stack, sign, curr_num)
        result = 0
        while True:
            last_element = stack.pop()
            if last_element in {"+", "-", "*", "/"}:
                self.modify_stack(stack, last_element, result)
                break
            result += last_element                
                            
                
        
