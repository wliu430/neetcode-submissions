import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        res = []

        def dfs(src):
            while adj[src]:
                dst = heapq.heappop(adj[src])
                dfs(dst)

            res.append(src)

        dfs("JFK")

        return res[::-1]