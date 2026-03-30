# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not self.isValidBST(root.left):
            return False
        
        if not self.isValidBST(root.right):
            return False

        if root.left:
            p = root.left
            while p:
                left_max = p.val
                p = p.right
            if left_max>=root.val:
                return False

        if root.right:
            p = root.right
            while p:
                right_min = p.val
                p = p.left
            if right_min <= root.val:
                return False

        return True

    5
   
    