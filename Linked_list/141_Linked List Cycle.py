# Methode 1: fast, slow
# Methode 2: hash set
# 
# from typing import Optional
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 return True
#         return False
#LeetCode 的 ListNode 默认是可以哈希的。

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = set()
        cur = head
        while cur:
            if cur in visit:
                return True
            visit.add(cur)
            cur = cur.next
        return False
