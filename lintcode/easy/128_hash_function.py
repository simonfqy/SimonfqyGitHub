'''
https://www.lintcode.com/problem/hash-function/description
'''

# Using the property of modulo arithmetic operation: (A mod C + B mod C) mod C = (A + B) mod C;
# (A mod C * B mod C) mod C = (A * B) mod C.
class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        MAGIC = 33
        sum_so_far = 0
        for char in key:
            sum_so_far = (ord(char) + MAGIC*(sum_so_far)%HASH_SIZE) % HASH_SIZE
            
        return sum_so_far
