# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # bottom-up
        
        # definition: is balanced or not
        def dfs(node):
            if not node:
                return True, 0
            #去想这个height. 就是这个height是从bottom up上来的 所以他一定有值
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            height = 1 + max(left_height, right_height)
            
            return balanced, height

        balanced, height = dfs(root)
        return balanced