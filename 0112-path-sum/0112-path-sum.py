# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = []
        if not root:
            return False
        def dfs(node,val):
            if node.left:
                dfs(node.left,val + node.left.val)
            if node.right:
                dfs(node.right,val + node.right.val)
            if not node.left and not node.right:
                ans.append(val) 
        dfs(root,root.val)
        return targetSum in ans