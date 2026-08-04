class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def backtracking(r, c, index):
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or board[r][c] != word[index]
                or (r, c) in visited
            ):
                return False
            
            if index == len(word) - 1:
                return True
            
            visited.add((r, c))

            found = (
                backtracking(r + 1, c, index + 1)
                or backtracking(r - 1, c, index + 1)
                or backtracking(r, c + 1, index + 1)
                or backtracking(r, c - 1, index + 1)
            )

            visited.remove((r, c))

            return found
        
        for row in range(rows):
            for col in range(cols):
                if backtracking(row, col, 0):
                    return True
        
        return False
