from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            digit = (carry+a+b) % 10
            carry = (a+b) // 10

            cur.next.val = digit
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


        

