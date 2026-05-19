class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Special case: only one house
        if n == 1:
            return nums[0]

        # Case 1: do not rob the first house
        money1 = self.rob_line(nums[1:])

        # Case 2: do not rob the last house
        money2 = self.rob_line(nums[:-1])

        return max(money1, money2)

    def rob_line(self, arr: List[int]) -> int:
        # dp[i] = max money you can rob from house i to the end
        n = len(arr)
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            dp[i] = max(
                arr[i] + dp[i + 2],  # rob current house
                dp[i + 1]            # skip current house
            )

        return dp[0]
