class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # 1) 终止条件：已经匹配到 word 的第 i 个字符；若 i==len(word)，说明前面全匹配成功
            if i == len(word):
                return True

            # 2) 当前格合法性检查（越界 / 字符不等 / 已经用过）
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            # 做选择：占用当前格
            path.add((r, c))

            # 3) 递归：向上下左右探索下一个字符；任一方向成功即可
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # 回退：撤销占用，恢复现场，便于其他分支使用这个格子，
            #就是这个格子走不通 所以直接remove
            path.remove((r, c))
            return res

        # 从任意起点尝试拼出 word
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False