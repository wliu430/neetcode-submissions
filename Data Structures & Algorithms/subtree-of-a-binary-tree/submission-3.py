# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(node1, node2):

            # 1. Termination
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            # 2. Process current nodes
            if node1.val != node2.val:
                return False
            # 3. Process child nodes
            left_same = isSame(node1.left, node2.left)
            right_same = isSame(node1.right, node2.right)
            return left_same and right_same

        def dfs(node):

            if not node:
                return False
            
            if isSame(node, subRoot):
                return True
            
            left_found = dfs(node.left)
            right_found = dfs(node.right)

            return left_found or right_found
        
        return dfs(root)
