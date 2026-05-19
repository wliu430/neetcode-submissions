# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # ===== ① Termination condition (Base case) =====
        if not root:
            return False

        # ===== ② Current node's own logic =====
        # 尝试：是否能从“当前节点”开始，完整匹配 subRoot
        if self.isSameTree(root, subRoot):
            return True

        # ===== ③ Recursive calls to subproblems =====
        # 当前节点不行，就去左右子树继续找“起点”
        left_is_sub = self.isSubtree(root.left, subRoot)
        right_is_sub = self.isSubtree(root.right, subRoot)

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