class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 1️⃣ 转置矩阵：沿主对角线对称交换
        for i in range(n):
            for j in range(i + 1, n):   # 注意从 i+1 开始避免重复交换
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2️⃣ 每一行反转（水平翻转）
        for row in matrix:
            row.reverse()