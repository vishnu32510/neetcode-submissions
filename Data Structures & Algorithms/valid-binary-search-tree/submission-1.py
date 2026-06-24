# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, greatest, smallest):
            if not node:
                return True
            
            if not (smallest < node.val < greatest):
                return False
            
            return dfs(node.left, node.val, smallest) and dfs(node.right, greatest, node.val)
        return dfs(root,  float('inf'), float('-inf'))