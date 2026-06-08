class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        path = []

        def backtrack(openN, closeN):
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            if openN < n:
                path.append("(")
                backtrack(openN + 1, closeN)
                path.pop()
            
            if closeN < openN:
                path.append(")")
                backtrack(openN, closeN + 1)
                path.pop()
        
        backtrack(0, 0)
        return res