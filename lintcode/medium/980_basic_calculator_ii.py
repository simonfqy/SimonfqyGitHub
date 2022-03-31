'''
Link: https://www.lintcode.com/problem/980
'''

# My own solution. This question was also asked during the MS VO in Mar 2022.
class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s: str) -> int:
        # global_result stores the results for addition and subtraction.
        global_result = 0
        # local_result stores the results for multiplication and division.
        local_result = 1
        global_sign = 1
        # local_sign can be None, "*" and "/".
        local_sign = None
        curr_number = 0
        for char in s:
            if char.isnumeric():
                curr_number = 10 * curr_number + int(char)
                continue
            if char == "+" or char == "-":
                global_result = self.calculate_global(global_result, global_sign, curr_number, local_sign, local_result)
                local_sign = None
                local_result = 1
                curr_number = 0
                global_sign = 1 if char == "+" else -1
            elif char == "*" or char == "/":
                local_result = self.calculate_local(local_result, local_sign, curr_number)
                local_sign = char
                curr_number = 0
        if local_sign:
            global_result = self.calculate_global(global_result, global_sign, curr_number, local_sign, local_result)
        elif curr_number != 0:
            global_result += curr_number * global_sign
        return global_result

    def calculate_global(self, global_result, global_sign, curr_number, local_sign, local_result):
        if not local_sign:
            global_result += curr_number * global_sign
            return global_result        
        local_result = self.calculate_local(local_result, local_sign, curr_number)
        global_result += local_result * global_sign
        return global_result

    def calculate_local(self, local_result, local_sign, curr_number):
        if not local_sign or local_sign == "*":
            local_result *= curr_number
        elif local_sign == "/":
            local_result = int(local_result/curr_number)
        return local_result

      
# My implementation based on the instruction from jiuzhang.com. Uses stack and is much more succinct than my solution above.
# We just need to sum up the elements inside the stack to get the final result.
class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s: str) -> int:
        stack = []
        curr_num = 0
        curr_operator = None
        for i, char in enumerate(s):
            if char.isnumeric():
                curr_num = curr_num * 10 + int(char)                
            if char in {"+", "-", "*", "/"} or i == len(s) - 1:
                self.modify_stack(stack, curr_operator, curr_num)
                curr_operator = char
                curr_num = 0          
        
        return sum(stack)

    def modify_stack(self, stack, curr_operator, curr_num):        
        if not curr_operator or curr_operator == "+" or curr_operator == "-":
            sign = -1 if curr_operator == "-" else 1
            stack.append(sign * curr_num)
            return        
        curr_res = stack.pop()
        if curr_operator == "*":            
            stack.append(curr_res * curr_num)
        elif curr_operator == "/":
            stack.append(int(curr_res / curr_num))
        return stack

    
# Solution from jiuzhang.com. Very similar to my solution above, but more succinct.
class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        if not s:
            return 0
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                # When we encounter "*" or "/", make sure that the last element in the stack is always the result of the
                # multiplication/division block.
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:                  
                    stack.append(int(stack.pop()/num))
                sign = s[i]
                num = 0
        return sum(stack)


    
