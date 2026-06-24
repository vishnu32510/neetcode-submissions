# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodnode = [0]
        
        def dfs(node, greatest):
            if not node:
                return 0
            
            if node.val >= greatest:
                goodnode[0] += 1
                greatest = node.val
            
            dfs(node.left, greatest)
            dfs(node.right, greatest)
        dfs(root,float('-inf'))
        return goodnode[0]