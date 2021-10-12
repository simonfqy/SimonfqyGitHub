'''
https://www.lintcode.com/problem/657/
'''

# My own solution. I feel this may not be a valid solution, because we convert a set to list in getRandom() which is likely an O(n)
# operation, where n is the size of the list/set.
import random
class RandomizedSet:
    
    def __init__(self):
        self.value_to_ind = dict()
        self.ind_to_value = dict()
        self.inactive_indices = set()
        self.active_indices = set()

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        if val in self.value_to_ind:
            return False
        if len(self.inactive_indices) > 0:
            for ind in self.inactive_indices:
                self.ind_to_value[ind] = val
                self.value_to_ind[val] = ind
                self.inactive_indices.remove(ind)
                self.active_indices.add(ind)
                return True
        new_ind = len(self.value_to_ind)
        self.value_to_ind[val] = new_ind
        self.ind_to_value[new_ind] = val
        self.active_indices.add(new_ind)
        return True        

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        if val not in self.value_to_ind:
            return False
        ind_of_element_for_removal = self.value_to_ind[val]
        self.inactive_indices.add(ind_of_element_for_removal)
        self.active_indices.remove(ind_of_element_for_removal)
        del self.ind_to_value[ind_of_element_for_removal]
        del self.value_to_ind[val]
        return True        

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        active_indices_list = list(self.active_indices)
        ind_of_choice = active_indices_list[random.randint(0, len(active_indices_list) - 1)]
        return self.ind_to_value[ind_of_choice]
    
    
# Also my own solution, but it makes use of random.choice() function directly and I'm not quite sure whether this is really permitted. 
# In fact, this solution is not correct, because converting set to list is not an O(1) operation.
import random
class RandomizedSet:
    
    def __init__(self):
        self.values = set()

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        if val in self.values:
            return False
        self.values.add(val)
        return True        

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        if val not in self.values:
            return False
        self.values.remove(val)
        return True        

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        return random.choice(list(self.values))
    
    
# The solution from jiuzhang.com. It is a valid solution. 
import random
class RandomizedSet(object):

    def __init__(self):
        # do initialize if necessary  
        self.nums, self.val_to_ind = [], dict()
        
    # @param {int} val Inserts a value to the set
    # Returns {bool} true if the set did not already contain the specified element or false
    def insert(self, val):
        if val in self.val_to_ind:
            return False
        self.val_to_ind[val] = len(self.nums)
        self.nums.append(val)
        return True
        
    # The most important operation. When I was working on the problem, I didn't come up with this idea
    # to migrate the last element to the position of the removed element. It ensures O(1) time complexity.
    def remove(self, val):
        if val not in self.val_to_ind:
            return False
        val_ind = self.val_to_ind[val]
        last_element = self.nums[-1]
        
        # move the last element to val_ind
        self.nums[val_ind] = last_element
        self.val_to_ind[last_element] = val_ind

        # remove the last element
        del self.val_to_ind[val]
        self.nums.pop()
        return True
    
    # return {int} a random number from the set
    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]
