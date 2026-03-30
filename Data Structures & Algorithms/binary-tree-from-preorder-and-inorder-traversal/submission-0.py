# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder root, left, right
        # inorder left, root, right
        n = len(preorder)
        if n == 0:
            return None

        root = preorder[0]
        index = -1
        for i in range(n):
            if inorder[i] == root:
                index = i
                break
        left_inorder = inorder[:i]
        right_inorder = inorder[i+1:]

        left_preorder = preorder[1:1+i]
        right_preorder = preorder[1+i:]

        return TreeNode(root,self.buildTree(left_preorder,left_inorder),self.buildTree(right_preorder,right_inorder))
        