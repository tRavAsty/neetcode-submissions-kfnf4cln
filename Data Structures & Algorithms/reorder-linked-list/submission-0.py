# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        print(nodes)
        l = 0
        r = len(nodes)-1
        res = ListNode()

        while l<=r:
            if l == r:
                cur = nodes[l]
                cur.next = None
                res.next = cur
                break
            left_node = nodes[l]
            right_node = nodes[r]
            left_node.next = right_node
            right_node.next = None
            res.next = left_node
            res = right_node
            l+=1
            r-=1  