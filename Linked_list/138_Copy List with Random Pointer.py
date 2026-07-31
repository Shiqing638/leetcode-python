# Methode 1: hash set
# Methode 2: space optimized

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         if not head:
#             return None

#         oldToNew = {}
#         cur = head
#         while cur:
#             oldToNew[cur] = Node(cur.val)
#             cur = cur.next

#         cur = head
#         while cur:
#             oldToNew[cur].next = oldToNew.get(cur.next)
#             oldToNew[cur].random = oldToNew.get(cur.random)
#             cur = cur.next

#         return oldToNew[head]

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next
#A -> A' -> B -> B' -> C -> C'
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next

        old = head
        new = head.next
        newHead = new

        while old:
            old.next = old.next.next
            if new.next:
                new.next = new.next.next
            old = old.next
            new = new.next

        return newHead

