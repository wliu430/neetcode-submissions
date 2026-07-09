class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length

                for last in range(left + 1, right):
                    coins = (
                        dp[left][last]
                        + dp[last][right]
                        + arr[left] * arr[last] * arr[right]
                    )

                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n - 1]