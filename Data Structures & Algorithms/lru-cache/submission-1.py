class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mem = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.mem:
            return -1
        curr = self.mem[key]
        self.move_to_head(curr,True)
        return curr.val

    def put(self, key: int, value: int) -> None:
        if key in self.mem:
            curr = self.mem[key]
            curr.val = value
            self.move_to_head(curr,True)
        else:
            curr = ListNode(key,value)
            self.move_to_head(curr,False)
            self.mem[key]=curr

        if len(self.mem)>self.capacity:
            tmp = self.pop_last()
            del self.mem[tmp.key]
    
    def move_to_head(self,node,existed=False):
        if existed:
            node_next = node.next
            node_prev = node.prev
            node_prev.next = node_next
            node_next.prev = node_prev
        
        tmp = self.head.next
        self.head.next = node

        node.prev = self.head
        node.next = tmp

        tmp.prev = node
        
    def pop_last(self):
        tmp = self.tail.prev
        last = tmp.prev

        last.next = self.tail
        self.tail.prev = last
        return tmp
    

        

            
        
class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
