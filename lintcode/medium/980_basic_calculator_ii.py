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

      
