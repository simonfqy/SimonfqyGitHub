'''
Link: https://www.lintcode.com/problem/209/
'''

# My own solution. Has O(n) time and space complexities, where n is the size of the input string. Uses 1 list and 2 sets.
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, string):
        element_order = []
        duplicate = set()
        singular = set()
        for char in string:
            if char in duplicate:
                continue
            if char in singular:
                singular.remove(char)
                duplicate.add(char)
                continue
            element_order.append(char)
            singular.add(char)
        for char in element_order:
            if char in singular:
                return char
              
              
