# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # balanced = True
        # def dfs(node):
        #     nonlocal balanced
        #     if not node:
        #         return 0

        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     if abs(left - right) > 1:
        #         balanced = False

        #     return 1 + max(left,right)
        # dfs(root)
        # return balanced

        def dfs(node):
            if not node:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            balanced = abs(left[1] - right[1]) <= 1 and left[0] and right[0]
            return [balanced, 1 + max(left[1], right[1]) ]
        return dfs(root)[0]