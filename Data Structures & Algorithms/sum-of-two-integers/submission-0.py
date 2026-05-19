class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 模拟32位整数范围
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        
        while b != 0:
            # 1️⃣ 无进位加法
            sum_ = (a ^ b) & mask
            # 2️⃣ 进位（注意左移）
            carry = ((a & b) << 1) & mask
            # 更新 a,b
            a, b = sum_, carry
        
        # 如果结果超过 32 位正数范围 → 转换为负数
        return a if a <= max_int else ~(a ^ mask)