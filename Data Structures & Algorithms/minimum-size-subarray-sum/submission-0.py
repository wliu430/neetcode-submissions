class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #expand right, shrink left

        l = 0
        resSum = 0
        minLen = float("inf")
        
        for r in range(len(nums)):

            resSum += nums[r]
            while resSum >= target:
                minLen = min(minLen, r - l + 1)
                
                resSum -= nums[l]
                l += 1
            
            
        
        return minLen if minLen != float("inf") else 0