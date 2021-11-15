'''
Link: https://www.lintcode.com/problem/722
'''


# Slightly modified from the solution from jiuzhang.com. Uses trie. Has O(n) time complexity, where n is the length of the array.
# It makes use of trie data structure, which makes string retrieval and comparison efficient. Otherwise it would be O(n^2). 
class TrieNode:
    def __init__(self):
        self.sons = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        node = self.root
        for i in range(30, -1, -1):
            digit = number >> i & 1
            if not node.sons[digit]:
                node.sons[digit] = TrieNode()
            node = node.sons[digit]

    # Each time we call get_largest_xor(), it will always reach a prefix value previously stored into the trie, which is maximally different from 
    # number, meaning that the found prefix value XOR number is the largest possible across all the prefix values stored in the trie. The returned
    # Result is that value. And the subarray yielding this maximum XOR value starts right after the found prefix value.
    def get_largest_xor(self, number):
        node = self.root
        result = 0
        for i in range(30, -1, -1):
            digit = number >> i & 1
            target = 1 - digit
            if node.sons[target]:
                result += 1 << i
                node = node.sons[target]
            else:
                node = node.sons[digit]
        return result

class Solution:
    """
    @param nums: the array
    @return: the max xor sum of the subarray in a given array
    """
    def maxXorSubarray(self, nums):
        trie = Trie()
        trie.insert(0)
        prefix_xor = 0
        max_xor = float('-inf')
        for num in nums:
            prefix_xor ^= num
            trie.insert(prefix_xor)
            max_xor = max(max_xor, trie.get_largest_xor(prefix_xor))
        return max_xor

        
