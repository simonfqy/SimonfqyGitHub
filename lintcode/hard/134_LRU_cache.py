'''
Link: https://www.lintcode.com/problem/134/
'''

# My own solution. Uses FIFO queue to implement, as well as hash maps.
from collections import deque, defaultdict
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_val = dict()
        self.key_queue = deque()
        self.key_to_count = defaultdict(int)

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.key_to_val:
            return -1
        value = self.key_to_val[key]
        self.key_queue.append(key)
        self.key_to_count[key] += 1
        self.remove_old_entries()
        return value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):        
        self.key_to_val[key] = value
        self.key_to_count[key] += 1
        self.key_queue.append(key)
        self.remove_old_entries()
    
    def remove_old_entries(self):
        while len(self.key_to_val) > self.capacity or self.key_to_count[self.key_queue[0]] > 1:
            old_item_key = self.key_queue.popleft()
            self.key_to_count[old_item_key] -= 1
            if self.key_to_count[old_item_key] == 0:
                del self.key_to_val[old_item_key] 
                
                
