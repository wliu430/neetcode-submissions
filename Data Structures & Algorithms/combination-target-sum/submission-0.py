class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # --- 1) 终止条件 ---
            if total == target:
                res.append(cur.copy())   # 记录一份路径拷贝
                return
            if i >= len(nums) or total > target:
                return                   # 越界 或 已经超过 target，剪枝返回

            # --- 2) 当前层处理：对第 i 个数做“要/不要”的二叉选择 ---
            # 选择“要”nums[i]（允许重复：所以递归时 i 不变）
            cur.append(nums[i])
            # --- 3) 递归 与 回退 ---
            dfs(i, cur, total + nums[i])  # 仍从 i 开始，表示还能继续用 nums[i]
            cur.pop()                      # 回退（撤销刚才加入的 nums[i]）

            # 选择“不要”nums[i]（跳到下一个候选）
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res