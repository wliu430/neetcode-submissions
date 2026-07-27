# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preorder_index = 0
        inorder_index = {value: index for index, value in enumerate(inorder)}

        def dfs(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)

            middle = inorder_index[root_val]

            root.left = dfs(left, middle - 1)
            root.right = dfs(middle + 1, right)

            return root

        return dfs(0, len(inorder) - 1)