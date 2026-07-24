# Methode 1: two pass
# Methode 2: fast slow pointer

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         length = 0
#         cur = head
#         while cur:
#             length += 1
#             cur = cur.next
        
#         if n == length:
#             return head.next
        
#         cur = head
        
#         for _ in range(length-n-1):
#             cur = cur.next
#         cur.next = cur.next.next

#         return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        while n:
            fast = fast.next
            n -= 1
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next

    
node1 = ListNode()
node2 = ListNode()
node3 = ListNode()

node1.val = 1
node1.next = node2
node2.val = 2
node2.next = node3
node3.val = 3
node3.next = None

sol = Solution()
res = sol.removeNthFromEnd(node1, 2)

cur = res
while cur:
    print(cur.val)
    cur = cur.next
