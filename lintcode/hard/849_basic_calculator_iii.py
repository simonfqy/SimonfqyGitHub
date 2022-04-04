'''
Link: https://www.lintcode.com/problem/849
'''

# My own solution. Uses stack.
# When we encounter "(", we push the sign (+, -, *, /) right before it into the stack. When we encounter ")", we pop all the way until the sign before the 
# "(" is removed from the stack. The only case where we push the sign (+, -, *, /) into the stack is when seeing parentheses. 
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
    
    # Refer to https://github.com/simonfqy/SimonfqyGitHub/blob/af5b30e7c1d5fceb6438837f0e497a0567af0b3d/lintcode/medium/980_basic_calculator_ii.py#L91.
    # This implementation is copied from that one.
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
              
              
# Solution from a student on jiuzhang.com.
# 用栈来存放之前的num 和 operator, 当前只保存一个number
# 基本逻辑: 当遇到一个新的operator时, 只要新的operator比栈顶的operator级别低, 弹栈并处理, 直到栈空, 或栈顶的operator级别低于当前.最后把处理的结果(一个数)和当前operator一并入栈.
# 对括号的处理: 1. '('直接入栈. 2. 弹栈时如果遇到'('则停止. 3. 如果遇到')', 则将栈中直到上一个'('的operation全部处理掉, 结果保存在当前number中, 最后将栈顶的'('弹出.
# 全部做完后最后再处理一下还在栈内的operation.
class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s: str) -> int:
        priority = {'+': 0, "-": 0, "*": 1, "/": 1}
        stack = []
        n = len(s)
        curr_num = 0        
        for i, char in enumerate(s):
            if char in "+-*/":                               
                while len(stack) and stack[-1] in priority and priority[stack[-1]] >= priority[char]:
                    curr_num = self.calculate_stack_end(stack, curr_num)
                # We only push the curr_num to the stack when char is "+-*/". 
                stack.append(curr_num)
                stack.append(char)                
                curr_num = 0                 
            elif char == "(":
                stack.append(char)
            elif char == ")":                
                while stack and stack[-1] != "(":
                    curr_num = self.calculate_stack_end(stack, curr_num)                
                stack.pop()                 
            elif char.isnumeric():
                curr_num = curr_num * 10 + int(char)     
                
        while stack:            
            curr_num = self.calculate_stack_end(stack, curr_num)
        return curr_num
    
    def calculate_stack_end(self, stack, curr_num):        
        sign = stack.pop()
        prev_num = stack.pop()
        return self.calculate_last_element(prev_num, sign, curr_num)

    def calculate_last_element(self, prev_num, sign, curr_num):
        if sign == "+":
            return prev_num + curr_num
        if sign == "-":
            return prev_num - curr_num
        if sign == "*":
            return prev_num * curr_num
        if sign == "/":
            return int(prev_num / curr_num)
        
        
        
