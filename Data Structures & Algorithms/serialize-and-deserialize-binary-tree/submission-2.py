# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    #preoder
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("null")
                return
            
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        index = 0

        def dfs():
            nonlocal index

            value = values[index]
            index += 1

            if value == "null":
                return None
            
            node = TreeNode(int(value))

            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()