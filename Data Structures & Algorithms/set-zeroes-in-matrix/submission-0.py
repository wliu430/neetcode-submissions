class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m, n = len(matrix), len(matrix[0])
        col0 = False  # 记录第一列是否需要清零

        # 1) 第一次遍历：设标记
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0      # 标记该行
                    matrix[0][j] = 0      # 标记该列

        # 2) 第二次遍历：根据标记清中间区域（不动首行首列）
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 3) 处理首行
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        # 4) 处理首列
        if col0:
            for i in range(m):
                matrix[i][0] = 0