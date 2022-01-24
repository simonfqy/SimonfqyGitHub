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
            
            
# Solution similar to jiuzhang.com. Has O(n) time complexity. Uses only 1 dictionary and 1 list.
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, string):
        char_to_freq = dict()
        elements = []
        for char in string:
            if char not in char_to_freq:
                char_to_freq[char] = 0
                elements.append(char)
            char_to_freq[char] += 1
        for char in elements:
            if char_to_freq[char] == 1:
                return char
            
            
# My own solution. Has O(n) time complexity. Uses an ordered dictionary.
from collections import OrderedDict
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, string):
        char_to_freq = OrderedDict()
        for char in string:
            if char not in char_to_freq:
                char_to_freq[char] = 0
            char_to_freq[char] += 1
        for char in char_to_freq:
            if char_to_freq[char] == 1:
                return char
            
            
# My own solution inspired by the instructions on jiuzhang.com. Uses a custom linked list, has O(n) time complexity, traverses through the string once. 
# Uses 1 dictionary to help with counting.
class LinkedNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.value_to_prev = dict()
        self.dummy = LinkedNode(None, None)
        self.tail = self.dummy

    def append(self, value):
        new_node = LinkedNode(value, None)
        self.tail.next = new_node
        self.value_to_prev[value] = self.tail
        self.tail = new_node

    def remove(self, value):
        prev_node = self.value_to_prev[value]
        node_to_remove = prev_node.next
        next_node = node_to_remove.next
        prev_node.next = next_node
        if node_to_remove != self.tail:          
            self.value_to_prev[next_node.value] = prev_node
            node_to_remove.next = None
        else:
            self.tail = prev_node
        del self.value_to_prev[value]

    def get_first_value(self):
        return self.dummy.next.value


class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, string):
        char_to_freq = dict()
        unique_char_list = LinkedList()
        for char in string:
            char_to_freq[char] = char_to_freq.get(char, 0) + 1
            if char_to_freq[char] == 1:
                unique_char_list.append(char)
            elif char_to_freq[char] == 2:
                unique_char_list.remove(char)
        return unique_char_list.get_first_value()
    
    
# Solution from a student on jiuzhang.com. Also implements a custom linked list, but the code is more succinct.
# It also offers protection against the case where there's no unique character in the string.
class Solution:
    
    def firstUniqChar(self, s):
        
        dummy = ListNode(None); tail = dummy
        tab, invalid = {}, object()
        for c in s:            
            if c not in tab:
                node = ListNode(c)
                tab[c], tail.next, tail = tail, node, node
            else:
                if tab[c] is invalid:
                    continue
                prv, nxt = tab[c], tab[c].next.next
                prv.next = nxt 
                if nxt:
                    tab[nxt.val] = prv
                else:
                    tail = prv
                tab[c] = invalid
            
        return dummy.next.val if dummy.next else '0'
    
