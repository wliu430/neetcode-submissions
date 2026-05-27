class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i, n in enumerate(s):
            last[n] = i
        
        start, end = 0, 0
        res = []

        for i, n in enumerate(s):
            end = max(end, last[n])

            if i == end:
                res.append(end - start + 1)
                start = i + 1
        
        return res