'''
https://www.lintcode.com/problem/954/
Leetcode link: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
'''

# My own solution. Similar to question 657:
# https://github.com/simonfqy/SimonfqyGitHub/blob/bd9f856eadd7e03cc44caf56ab3ca6b879fd775d/lintcode/medium/657_insert_delete_getrandom_O(1).py#L96,
# but here we let each value map to a set of indices, since we allow duplicate values. This implementation should have O(1) time complexity for
# each operation.
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_to_index_set = dict()
        self.values = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        return_bool = val not in self.val_to_index_set
        if return_bool:
            self.val_to_index_set[val] = set()
        self.val_to_index_set[val].add(len(self.values))
        self.values.append(val)
        return return_bool
        
    # This function is actually incorrect. It fails the leetcode test cases (though it passes the lintcode one).
    def remove_incorrect(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_index_set:
            return False
        index_set = self.val_to_index_set[val]
        last_val = self.values[-1]
        # copy the last value to a random index of the val to be removed.
        pos_to_replicate_last_val = next(iter(index_set))
        self.values[pos_to_replicate_last_val] = last_val
        self.val_to_index_set[last_val].remove(len(self.values) - 1)
        self.val_to_index_set[last_val].add(pos_to_replicate_last_val)

        self.val_to_index_set[val].remove(pos_to_replicate_last_val)
        if len(self.val_to_index_set[val]) == 0:
            del self.val_to_index_set[val]
        self.values.pop()
        return True        
    
    # This function is the correct implementation for remove() function. It passes all leetcode tests. The important thing to note
    # is that, we have to separately consider the cases where the self.values[-1] equals the value to be removed and where it doesn't.
    # This complexity is due to the permission of duplication.
    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_index_set:
            return False
        index_set = self.val_to_index_set[val]
        last_val = self.values[-1]        
        if last_val != val:
            # copy the last value to a random index of the val to be removed.
            pos_to_replicate_last_val = next(iter(index_set))
            self.values[pos_to_replicate_last_val] = last_val
            self.val_to_index_set[last_val].remove(len(self.values) - 1)
            self.val_to_index_set[last_val].add(pos_to_replicate_last_val)
            self.val_to_index_set[val].remove(pos_to_replicate_last_val)
        else:
            self.val_to_index_set[val].remove(len(self.values) - 1)
            
        if len(self.val_to_index_set[val]) == 0:
            del self.val_to_index_set[val]
        self.values.pop()
        return True
    
    # This is also a correct implementation without needing to consider separate cases using if statements. The code logic is a bit fragile, because
    # the order of lines of code matters, it is not easy to get the order right in the first trial.
    # The gist of the story is that, explicitly using if statement to separate the concerns is more desirable and easier.
    def remove_2(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_index_set:
            return False
        index_set = self.val_to_index_set[val]
        last_val = self.values[-1]
        # copy the last value to a random index of the val to be removed.
        pos_to_replicate_last_val = next(iter(index_set))
        self.values[pos_to_replicate_last_val] = last_val
        
        # The order of the 3 lines below truly matters. It is a bit fragile.
        self.val_to_index_set[val].remove(pos_to_replicate_last_val)        
        self.val_to_index_set[last_val].add(pos_to_replicate_last_val)
        self.val_to_index_set[last_val].remove(len(self.values) - 1)
        
        if len(self.val_to_index_set[val]) == 0:
            del self.val_to_index_set[val]
        self.values.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.values)
    
    
# The solution below is for leetcode. It is from jiuzhang.com, and I translated it from Java to Python. It is rather complicated and
# hard to think of. Took me tremendous effort to understand and translate it.
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_to_index_list = dict()
        self.values_and_indices = []        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        return_bool = val not in self.val_to_index_list
        if return_bool:
            self.val_to_index_list[val] = []
        # Each tuple stored in self.values_and_indices is the value and the order number of the current value among all its occurrences.
        # For example, we can have a list with values [4, 2, 4, 4], for which self.values_and_indices would be [(4, 0), (2, 0), (4, 1), (4, 2)].
        # In the last tuple (4, 2), 4 is the value, while 2 means it is the 2nd 4 (the order starts from 0). The corresponding self.val_to_index_list[4]
        # is [0, 2, 3]. 
        # So how is it used? In the remove() function, if we are removing 4 from a list of values [4, 2, 4, 1, 1], originally self.val_to_index_list[1]
        # is [3, 4], now it becomes [3, 2], since we move the last element to the position where we want the element removed. The ending list becomes
        # [4, 2, 1, 1], where the first 1 with index 2 is actually the original second 1. The original first 1 is unchanged, we only move the second
        # 1 to the front.
        self.values_and_indices.append((val, len(self.val_to_index_list[val])))
        self.val_to_index_list[val].append(len(self.values_and_indices) - 1)        
        return return_bool        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_index_list:
            return False
        index_list_of_removing_element = self.val_to_index_list[val]
        last_ind_of_removing_element = index_list_of_removing_element[-1]
        # Copy the last element to the position to substitute the one to be removed.
        last_val_and_index = self.values_and_indices[-1]
        self.values_and_indices[last_ind_of_removing_element] = last_val_and_index        
        self.val_to_index_list[last_val_and_index[0]][last_val_and_index[1]] = last_ind_of_removing_element
        self.val_to_index_list[val].pop()
        if not self.val_to_index_list[val]:
            del self.val_to_index_list[val]     
        self.values_and_indices.pop()        
        return True         

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.values_and_indices)[0]
