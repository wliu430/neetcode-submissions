import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 1. 按区间左端点排序
        intervals.sort()
        
        # 2. 查询排序，但保留原下标
        queries_with_idx = sorted([(q, i) for i, q in enumerate(queries)])
        
        res = [-1] * len(queries)
        heap = []  # (interval_length, right)
        i = 0      # 指向 intervals 的指针
        
        # 3. 逐个处理 query（从小到大）
        for q, idx in queries_with_idx:
            
            # 把所有 left <= q 的区间加入 heap
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                i += 1
            
            # 移除已经不能覆盖 q 的区间（right < q）
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            # 当前 heap 顶部就是最短可用区间
            if heap:
                res[idx] = heap[0][0]
            else:
                res[idx] = -1
        
        return res
