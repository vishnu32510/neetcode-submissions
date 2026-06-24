# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not q and not p:
                return True
            if not q or not p:
                return False

            if q.val != p.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        # isSubroot = False
        # def dfs(node):
        #     nonlocal isSubroot
        #     if not node:
        #         return

        #     isSubroot = isSubroot or isSameTree(node, subRoot)

        #     dfs(node.left)
        #     dfs(node.right)
        #     return 
        # dfs(root)
        # return isSubroot

        def dfs(node):
            if not node:
                return False
            if isSameTree(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        return dfs(root)

            