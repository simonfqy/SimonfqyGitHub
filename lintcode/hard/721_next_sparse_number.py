'''
Link: https://www.lintcode.com/problem/721
'''

# My own solution. Uses binary manipulation and two pointer.
class Solution:
    """
    @param x: a number
    @return: return the next sparse number behind x
    """
    def nextSparseNum(self, x):
        x_binary = self.convert_to_binary(x)
        if self.is_sparse(x_binary):
            return x
        n = len(x_binary)
        pos_rightmost_consecutive_zero = 0
        for i in range(1, n):
            if x_binary[i] == '1' and x_binary[i - 1] == '1':
                break
            if x_binary[i] == '0' and x_binary[i - 1] == '0':
                pos_rightmost_consecutive_zero = i
        # Get the converted binary.
        next_sparse = x_binary[:pos_rightmost_consecutive_zero] + '1' + '0' * (n - 1 - pos_rightmost_consecutive_zero)
        return self.convert_to_decimal(next_sparse)
    
    # convert number to a binary string.
    def convert_to_binary(self, num):
        binary = ""
        i = 0
        while 2 ** i <= num:
            binary = str((num >> i) & 1) + binary
            i += 1
        if not binary or binary[0] != "0": 
            binary = "0" + binary
        return binary

    def is_sparse(self, binary):
        n = len(binary)
        for i in range(1, n):
            if binary[i] == '1' and binary[i - 1] == '1':
                return False
        return True

    def convert_to_decimal(self, binary):
        result = 0
        n = len(binary)
        for i in range(n - 1, -1, -1):
            result += int(binary[i]) << (n - 1 - i)
        return result
      
