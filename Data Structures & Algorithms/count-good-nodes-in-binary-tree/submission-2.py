# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            current_good = 1 if node.val >= max_so_far else 0
            new_max = max(node.val, max_so_far)

            left_good = dfs(node.left, new_max)
            right_good = dfs(node.right, new_max)

            return current_good + left_good + right_good
        
        return dfs(root, root.val)