# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):

            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False

            left_valid = validate(node.left, min_val, node.val)
            right_valid = validate(node.right, node.val, max_val)


            return left_valid and right_valid
        
        return validate(root, float("-inf"),float("inf"))