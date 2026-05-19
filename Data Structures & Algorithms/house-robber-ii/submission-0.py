class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_line(arr):
            next1 = 0
            next2 = 0
            for x in reversed(arr):
                cur = max(x + next2, next1)
                next1, next2 = cur, next1
            return next1
        
        return max(nums[0], rob_line(nums[1:]), rob_line(nums[:-1]))