class Solution:
    def combinationSum(self, nums, target):
        res = []
        path = []

        def backtrack(start, remain):
            # ===== ① Termination condition =====
            if remain == 0:
                res.append(path.copy())
                return
            
            if remain < 0:
                return

            # ===== ② Current level logic =====
            for i in range(start, len(nums)):
                path.append(nums[i])

                # ===== ③ Recursive calls =====
                backtrack(i, remain - nums[i])

                path.pop()

        backtrack(0, target)
        return res
