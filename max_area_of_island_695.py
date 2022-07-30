class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = set()
        largest = 0
        r_len = len(grid)
        c_len = len(grid[0])
        for r in range(r_len):
            for c in range(c_len):
                size = self.explore(self, grid, r, c, visited)
                if size > largest:
                    largest = size
        return largest

    def explore(self, grid, r, c, visited):
        r_inbounds = 0 <= r < len(grid)
        c_inbounds = 0 <= c < len(grid[0])
        if not r_inbounds or not c_inbounds:
            return 0
        if grid[r][c] == 0:
            return 0
        if tuple((r, c)) in visited:
            return 0
        visited.add(tuple((r, c)))
        size = 1

        size += self.explore(self, grid, r-1, c, visited)  # up
        size += self.explore(self, grid, r+1, c, visited)  # down
        size += self.explore(self, grid, r, c-1, visited)  # left
        size += self.explore(self, grid, r, c+1, visited)  # #right

        return size
