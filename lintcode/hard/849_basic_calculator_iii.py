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
                

# My own solution, but largely inspired by the idea from jiuzhang.com. Uses a recursive solution.
class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s: str) -> int:
        # It is better as a global variable like here, rather than an input parameter. 
        # Because next_ind never goes back, only forward.
        self.next_ind = 0
        return self.calculate_recursively(s)
        
    def calculate_recursively(self, s):
        stack = []
        n = len(s)
        num = 0
        sign = "+"
        while self.next_ind < n:
            char = s[self.next_ind]
            if char.isnumeric():
                num = num * 10 + int(char)
                self.next_ind += 1
            elif char == "(":
                self.next_ind += 1
                num = self.calculate_recursively(s)
            elif char == ")":
                self.calculate_last_elements(stack, num, sign)
                self.next_ind += 1
                # Whenever we encounter a closing parenthesis, we stop the current recursion and return the result.
                return sum(stack)
            elif char in "+-*/":
                self.calculate_last_elements(stack, num, sign)
                sign = char
                num = 0
                self.next_ind += 1     
            else:
                self.next_ind += 1       
        
        # We don't have a closing parenthesis encountered in the current recursion level.         
        self.calculate_last_elements(stack, num, sign)

        return sum(stack)

    def calculate_last_elements(self, stack, num, sign):
        if sign == "+":
            stack.append(num)
        elif sign == "-":
            stack.append(-num)
        elif sign == "*":
            stack.append(stack.pop() * num)
        elif sign == "/":
            stack.append(int(stack.pop() / num))                          
              
              