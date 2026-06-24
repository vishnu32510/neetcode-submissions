# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS Iterative (O(n), O(n))
        if not root:
            return root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


        # DFS Iterartive (O(n), O(n))
        # if not root:
        #     return root
        
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     node.left, node.right = node.right, node.left

        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return root

        # DFS (O(n), O(n))
        # def dfs(node):
        #     if not node:
        #         return

        #     node.left, node.right = node.right, node.left

        #     dfs(node.left)
        #     dfs(node.right)
        
        # dfs(root)
        # return root