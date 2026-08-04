class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []

        def backtracking(index, remaining):

            if remaining == 0:
                result.append(combination.copy())
                return

            if index == len(nums) or remaining < 0:
                return
            
            #choose nums[index]
            combination.append(nums[index])
            backtracking(index, remaining - nums[index])
            combination.pop()

            #not choose
            backtracking(index + 1, remaining)
        
        backtracking(0, target)
        return result