from typing import List

class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:
        INF = float("inf")

        prices = [INF] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices.copy()

            for s, d, p in flights:
                if prices[s] == INF:
                    continue

                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p

            prices = temp

        return -1 if prices[dst] == INF else prices[dst]