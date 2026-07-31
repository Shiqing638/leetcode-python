# hashmap + double linked list
class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = {}

        self.left = self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def insert(self, node):
        prv = self.right.prev
        nxt = self.right
        prv.next = node
        nxt.prev = node
        node.prev = prv
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) ->None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]