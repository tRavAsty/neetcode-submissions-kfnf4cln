# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode()
        p = res_head
        carrier = 0
        while l1 or l2 or carrier!=0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            cur = v1+v2+carrier
            node = ListNode(cur%10)
            carrier = cur//10

            p.next = node
            p = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return res_head.next



        