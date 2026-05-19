class Solution:
    def rob(self, nums):
        next1 = 0  # dp[i+1]，初始为 dp[n] = 0
        next2 = 0  # dp[i+2]，初始为 dp[n+1] = 0

        # 从右往左：i = n-1, n-2, ..., 0
        for x in reversed(nums):
            # 当前最优：抢当前 + dp[i+2] 或 不抢 + dp[i+1]
            cur = max(x + next2, next1)

            # 左移窗口：为下一轮（更左边的 i-1）做准备
            next2, next1 = next1, cur

        # 循环结束，next1 就是 dp[0]
        return next1
