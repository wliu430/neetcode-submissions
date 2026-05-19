class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] 表示：走到第 i 阶，一共有多少种走法
        dp = [0] * (n + 1)

        # base cases
        dp[0] = 1  # 什么都不走，也是一种方式
        dp[1] = 1  # 只能走 1 步

        # 从第 2 阶开始推
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
