# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res_head = ListNode()
        res_head.next = head
        to_move=end=head
        prev = res_head

        for i in range(n):
            prev_end = end
            end = end.next
        
        while end:
            prev_end = end
            end = end.next
            to_move = to_move.next
            prev = prev.next
        
        prev.next = to_move.next

        return res_head.next

        
        