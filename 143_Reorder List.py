# Methode 1: list
# Methode 2: fast slow point
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         nodes = []
#         cur = head

#         while cur:
#             nodes.append(cur)
#             cur = cur.next

#         l = 0
#         r = len(nodes) - 1

#         while l < r:
#             nodes[l].next = nodes[r]
#             l += 1

#             if l == r:
#                 break

#             nodes[r].next = nodes[l]
#             r -= 1

#         nodes[l].next = None

        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:  
        if not head or not head.next:
            return 

        # 1. find middle point
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse
        second = slow.next  # curr = head
        slow.next = None  

        prev = second
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp 

        # 3. merge
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

        



