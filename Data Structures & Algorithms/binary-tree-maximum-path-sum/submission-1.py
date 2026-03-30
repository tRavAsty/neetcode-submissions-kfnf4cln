class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = float('-inf')
        def dfs(node:Optional[TreeNode]):
            nonlocal max_val
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            price_newpath = node.val + left + right
            max_val = max(max_val, price_newpath)
            
            return node.val + max(left, right)
        
        dfs(root)
        return max_val