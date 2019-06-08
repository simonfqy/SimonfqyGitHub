'''
Link: https://www.lintcode.com/problem/1-bit-and-2-bit-characters/description
'''

# My own solution.
class Solution:
    """
    @param bits: a array represented by several bits. 
    @return: whether the last character must be a one-bit character or not
    """
    def isOneBitCharacter(self, bits):
        # Write your code here
        if len(bits) == 0:
            return True
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
                continue
            if bits[i] == 1:
                if i + 1 == len(bits) - 1:
                    return False
                i += 2
        return True
