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
            
         
# My own solution. Similar to the one above, but much more modularized. 
class ListNode:
    def __init__(self, key=None, value=None, next_pointer=None):
        self.key = key
        self.value = value
        self.next_pointer = next_pointer

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = ListNode()
        self.tail = self.head
        self.key_to_prev_node = dict()

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.key_to_prev_node:
            return -1        
        self.move_to_tail(key)
        return self.tail.value        

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key not in self.key_to_prev_node:
            self.add_to_tail(ListNode(key=key, value=value))            
            self.evict_old()
        else:
            self.move_to_tail(key)
            self.tail.value = value

    # Move the node with key == key to the tail of the list.
    def move_to_tail(self, key):
        # Don't need to change anything if key is already the tail's key.
        if key == self.tail.key:
            return
        node_to_move = self.remove_from_list(key)
        self.add_to_tail(node_to_move)
    
    # Remove and return a node from the linked list.
    def remove_from_list(self, key):
        prev_node = self.key_to_prev_node[key]
        curr_node = prev_node.next_pointer
        del self.key_to_prev_node[key]
        next_node = curr_node.next_pointer
        if next_node and next_node.key is not None:
            self.key_to_prev_node[next_node.key] = prev_node
        prev_node.next_pointer = next_node
        curr_node.next_pointer = None
        return curr_node

    def add_to_tail(self, new_tail_node):
        self.key_to_prev_node[new_tail_node.key] = self.tail
        self.tail.next_pointer = new_tail_node
        new_tail_node.next_pointer = None
        self.tail = new_tail_node      

    def evict_old(self):
        if len(self.key_to_prev_node) <= self.capacity:
            return
        self.remove_from_list(self.head.next_pointer.key)        
        
        
# Solution from jiuzhang.com. In reality it's doing the same thing as my own implementation above.       
class LinkedNode:
    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity
    
    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        # 删除头部
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        
    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):	#将数据移动至尾部
        node = prev.next
        if node == self.tail:
            return
        
        # remove the current node from linked list
        prev.next = node.next
        # update the previous node in hash map
        self.key_to_prev[node.next.key] = prev
        node.next = None

        self.push_back(node)

    # @return an integer
    def get(self, key):
        if key not in self.key_to_prev:
            return -1
        
        prev = self.key_to_prev[key]
        current = prev.next
        
        self.kick(prev)
        return current.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.key_to_prev:	   
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
            return
        
        self.push_back(LinkedNode(key, value))  #如果key不存在，则存入新节点
        if len(self.key_to_prev) > self.capacity:		#如果缓存超出上限
            self.pop_front()	
            
            
