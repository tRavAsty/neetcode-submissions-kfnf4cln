# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res_head = res
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val<=p2.val:
                res.next = p1
                res = p1
                p1 = p1.next
            else:
                res.next = p2
                res = p2
                p2 = p2.next
        if p1:
            res.next = p1

        if p2:
            res.next = p2
        
        return res_head.next
            
        