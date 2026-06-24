# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            stack.append(node.val)
            dfs(node.right)
        dfs(root)
        res = 0
        return stack[k - 1] 
        
        # Brute Force (O(n log(n)), O(n))
        # q = []

        # def dfs(node):
        #     if not node:
        #         return
            
        #     heapq.heappush(q, node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # res = 0
        # for i in range(k):
        #     res = heapq.heappop(q)
        # return res 
