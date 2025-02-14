# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return []
        def dfs(node,arr):
            if node.left:
                dfs(node.left,arr+[node.left.val])
            if node.right:
                dfs(node.right,arr+[node.right.val])
            if not node.left and not node.right:
                ans.append(arr)
        dfs(root,[root.val])
        ans = [i for i in ans if sum(i)==targetSum]
        return ans