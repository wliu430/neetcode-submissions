import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while minHeap:
            time, r, c = heapq.heappop(minHeap)

            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or
                    nc < 0 or
                    nr >= n or
                    nc >= n or
                    (nr, nc) in visited
                ):
                    continue

                visited.add((nr, nc))
                newTime = max(time, grid[nr][nc])
                heapq.heappush(minHeap, (newTime, nr, nc))