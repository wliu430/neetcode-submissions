class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        max_len = max((len(w) for w in words), default=0)

        dp = [False] * (n + 1)
        dp[0] = True  # 空串为真

        for i in range(1, n + 1):
            # 只回看至多 max_len 个字符
            start = max(0, i - max_len)
            for j in range(start, i):
                # 前缀可达 且 后缀是词
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break  # 提前结束，i 已经为真
        return dp[n]