class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        def canFinish(k):
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            return hours <= h
        
        res = right

        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res