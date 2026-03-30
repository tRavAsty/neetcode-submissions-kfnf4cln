# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = []
        res = []
        if not root:
            return res
        queue = deque([root,"#"])
        while queue:
            cur = queue.popleft()
            if cur == "#":
                res.append(level)
                level = []
                if queue:
                    queue.append("#")
            else:
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
            
        