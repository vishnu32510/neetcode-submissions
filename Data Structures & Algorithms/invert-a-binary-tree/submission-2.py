# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # ##DFS
        # def dfs(node):
        #     if not node:
        #         return 

        #     node.left, node.right = node.right, node.left

        #     dfs(node.left)
        #     dfs(node.right)
        
        # dfs(root)
        # return root

        #BFS
        if not root:
            return root
        q = deque([root])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root

        #Iterative DFS
        # if not root:
        #     return root

        # stack = [root]
        # while stack:
        #     node = stac