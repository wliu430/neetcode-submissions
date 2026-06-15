import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        res = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            res = max(res, time)

            for nei, neiTime in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time + neiTime, nei))

        return res if len(visited) == n else -1