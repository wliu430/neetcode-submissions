class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            
            leftBalanced, leftHeight = dfs(node.left)
            rightBalanced, rightHeight = dfs(node.right)

            balenced = leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1
            height = max(leftHeight, rightHeight) + 1

            return [balenced, height]
        
        b, h = dfs(root)
        return b

