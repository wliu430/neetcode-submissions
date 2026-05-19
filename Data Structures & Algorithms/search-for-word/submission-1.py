class Solution:
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, idx):
            # ===== ① Termination condition =====
            # Case 1: all characters matched
            if idx == len(word):
                return True
            
            # Case 2: out of bounds or mismatch
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != word[idx]
            ):
                return False

            # ===== ② Current level logic =====
            # mark current cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # ===== ③ Recursive calls =====
            # try all four directions
            found = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )

            # backtrack: restore the cell
            board[r][c] = temp
            return found

        # try every cell as a starting point
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False
