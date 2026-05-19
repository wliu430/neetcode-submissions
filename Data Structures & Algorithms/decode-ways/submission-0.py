class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i+1], dp[i+2] 两个滚动变量
        next1, next2 = 1, 0   # 初始化：dp[n]=1，dp[n+1]=0(占位)
        # 从右往左
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                cur = 0
            else:
                cur = next1  # 取一位
                # 取两位（10..26）
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                    cur += next2
            # 左移窗口
            next1, next2 = cur, next1
        return next1