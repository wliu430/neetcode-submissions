class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # 1) 初始：每个位置单独成序列，长度为 1
        dp = [1] * n

        # 2) 双层循环，i 扩展自身结尾的最优
        for i in range(n):
            for j in range(i):
                # 只在严格递增时更新
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # 3) 全局最大
        return max(dp)