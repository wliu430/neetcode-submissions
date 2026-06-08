class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target:
                return 
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, nums[i] + total)
                path.pop()
            
        backtrack(0, 0)

        return res