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
                
                
# My implementation based on the __init__() functions provided by jiuzhang.com. Uses singly linked list with head and tail pointers, 
# as well as hash maps.
class LinkedNode:
    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_prev = dict()
        self.dummy = LinkedNode()
        self.tail = self.dummy        

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.key_to_prev:
            return -1
        self.move_to_end_of_list(key)
        return self.tail.value        

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key not in self.key_to_prev:
            curr_node = LinkedNode(key=key, value=value)
            prev_node = self.tail
            prev_node.next = curr_node
            self.key_to_prev[key] = prev_node
            self.tail = curr_node
            self.evict_old()
        else:
            self.move_to_end_of_list(key) 
            self.tail.value = value     

    def move_to_end_of_list(self, key):
        prev_node = self.key_to_prev[key]
        target_node = prev_node.next            
        next_node = target_node.next            
        if next_node:
            # Originally the target_node is not at the end of the linked list.
            prev_node.next = next_node
            self.key_to_prev[next_node.key] = prev_node
            self.key_to_prev[target_node.key] = self.tail  
            # Initially forgot about this assignment to overwrite self.tail.next.          
            self.tail.next = target_node
            target_node.next = None
            self.tail = target_node
    
    def evict_old(self):
        if len(self.key_to_prev) > self.capacity:
            head_node = self.dummy.next
            new_head = head_node.next
            self.dummy.next = new_head
            self.key_to_prev[new_head.key] = self.dummy
            head_node.next = None
            del self.key_to_prev[head_node.key]
            
            
