class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrack(start, goal):
            if goal == target:
                res.append(path.copy())
                return

            if goal > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, goal + candidates[i])
                path.pop()
        
        backtrack(0, 0)
        return res