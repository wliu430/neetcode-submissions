class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0

        def dfs(r, c):
            if(
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or grid[r][c] != "1"
                or (r, c) in visited
            ):
                return
            
            grid[r][c] = "0"
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    island += 1
                    dfs(r, c)
        

        return island