class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        cnt = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or
                    nc < 0 or
                    nr >= rows or
                    nc >= cols or
                    grid[nr][nc] != 1
                ):
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                cnt = grid[nr][nc] - 2
                q.append((nr, nc))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return cnt
            

        