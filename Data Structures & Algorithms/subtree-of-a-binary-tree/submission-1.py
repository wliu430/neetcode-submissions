# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #第一段
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True

        #第二段
        left_is_sub = self.isSubtree(root.left, subRoot)
        right_is_sub = self.isSubtree(root.right, subRoot)

        #第三段
        return left_is_sub or right_is_sub

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same