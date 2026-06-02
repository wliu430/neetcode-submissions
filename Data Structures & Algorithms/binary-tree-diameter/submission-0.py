# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            # 1. Termination condition
            if not node:
                return 0

            # 2. Recursive calls to child nodes
            left = dfs(node.left)
            right = dfs(node.right)

            # 3. Current node's own logic
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res