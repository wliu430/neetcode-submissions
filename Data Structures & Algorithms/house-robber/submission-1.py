class Solution:
    def rob(self, nums):
        n = len(nums)

        # dp[i] = max money from house i to the end
        dp = [0] * (n + 2)  # 多留两个位置，避免越界

        for i in range(n - 1, -1, -1):
            dp[i] = max(
                nums[i] + dp[i + 2],  # 抢当前
                dp[i + 1]             # 不抢当前
            )

        return dp[0]
