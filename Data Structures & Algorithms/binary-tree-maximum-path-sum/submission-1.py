# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):

            nonlocal res
            #termination
            if not node:
                return 0
            
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            cur_path_sum = node.val + left_gain + right_gain
            res = max(res, cur_path_sum)

            return max(left_gain, right_gain) + node.val
        
        dfs(root)
        return res
            
