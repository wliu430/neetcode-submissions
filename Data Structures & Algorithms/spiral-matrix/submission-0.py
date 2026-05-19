class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        res = []
        top, bottom, left, right = 0, m - 1, 0, n - 1

        while top <= bottom and left <= right:
            # →: top 行
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # ↓: right 列
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # ←: bottom 行（需再次检查边界）
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # ↑: left 列（需再次检查边界）
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res   