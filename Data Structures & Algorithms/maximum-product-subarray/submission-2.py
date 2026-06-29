class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        dpMax = [0] * n
        dpMin = [0] * n

        dpMax[0] = nums[0]
        dpMin[0] = nums[0]

        res = nums[0]

        for i in range(1, n):
            num = nums[i]

            dpMax[i] = max(
                num,
                dpMax[i - 1] * num,
                dpMin[i - 1] * num
            )

            dpMin[i] = min(
                num,
                dpMax[i - 1] * num,
                dpMin[i - 1] * num
            )

            res = max(res, dpMax[i])

        return res