'''
https://www.lintcode.com/problem/685/
'''

# My own solution. The efficiency is not great, but much better than my initial version which maintains a list of candidate unique
# numbers. Whenever we do a remove() operation the time complexity is O(n). Now with dictionary, the del time complexity is O(1).
# This solution only traverses through the nums stream once.
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        terminating_number_found = False
        candidate_unique_numbers_to_ind = dict()
        ind_to_candidate_unique_numbers = dict()
        repeated_numbers = set()
        for i, num in enumerate(nums):            
            if num in repeated_numbers:
                continue
            if num in candidate_unique_numbers_to_ind:
                index = candidate_unique_numbers_to_ind[num]
                del candidate_unique_numbers_to_ind[num]
                del ind_to_candidate_unique_numbers[index]
                repeated_numbers.add(num)
                continue
            candidate_unique_numbers_to_ind[num] = i
            ind_to_candidate_unique_numbers[i] = num
            if num == number:
                terminating_number_found = True
                break
        
        if not terminating_number_found:
            return -1
        return ind_to_candidate_unique_numbers[min(ind_to_candidate_unique_numbers.keys())]
        
        
# Based on an answer from jiuzhang.com. Traverses the array twice.
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        terminating_number_found = False
        counter = dict()
        for num in nums:
            if num in counter and counter[num] > 1:
                continue
            # Notice that we can use dict.get(key, default_val) to supply a default value if the key doesn't exist yet.
            counter[num] = counter.get(num, 0) + 1
            if num == number:
                terminating_number_found = True
                break
        if not terminating_number_found:
            return -1
        for num in nums:
            if counter[num] == 1:
                return num    
            
            
# Solution from a student on jiuzhang.com. Takes advantage of OrderedDict() class which can preserve the order of
# elements when they were added.
from collections import OrderedDict
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        unique_nums = OrderedDict()
        duplicate_nums = set()
        for num in nums:
            if num in duplicate_nums:
                continue
            if num in unique_nums:
                duplicate_nums.add(num)
                del unique_nums[num]
                continue
            unique_nums[num] = None
            if num == number:
                # The boolean argument indicates whether we should pop the last item. It defaults to True. If set
                # to False, it would pop the first item.
                item = unique_nums.popitem(False)
                return item[0]
        return -1
    
    
# A solution from a student on jiuzhang.com. Implemented using Python dictionary (hashmap) and linked list.
# Only traverses the list once. The elements in the linked list are candidate unique numbers. The first in the linked list
# is the first unique number.
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        self.initialize()
        val_to_node = dict()
        terminating_number_found = False
        for val in nums:
            if val not in val_to_node:
                new_node = Node(val)
                val_to_node[val] = new_node
                self.add_to_end(new_node)
            elif val_to_node[val]:
                node = val_to_node[val]
                val_to_node[val] = None
                self.remove(node)
            if val == number:
                terminating_number_found = True
                break
        if not terminating_number_found:
            return -1
        return self.head.next.val          
        
    def initialize(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_end(self, new_node):
        prev = self.tail.prev
        prev.next = new_node
        new_node.prev = prev
        new_node.next = self.tail
        self.tail.prev = new_node

    def remove(self, node):
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev
