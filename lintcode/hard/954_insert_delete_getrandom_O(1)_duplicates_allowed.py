'''
https://www.lintcode.com/problem/954/
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

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.values)
