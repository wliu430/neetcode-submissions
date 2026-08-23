class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    nr < 0
                    or nc < 0
                    or nr >= rows
                    or nc >= cols
                    or (nr, nc) in visited
                    or heights[nr][nc] < heights[r][c]
                ):
                    continue
                
                dfs(nr, nc, visited)

        for c in range(cols):
            dfs(0, c, pacific)
        
        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        res = []
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append((r, c))
        return res
