class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        
        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or board[r][c] != "O"
            ):
                return
            
            board[r][c] = "T"

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                dfs(nr, nc)
        
        for r in range(rows):
            dfs(r, 0)
        
        for c in range(cols):
            dfs(0, c)
        
        for r in range(rows):
            dfs(r, cols - 1)
        
        for c in range(cols):
            dfs(rows - 1, c)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"