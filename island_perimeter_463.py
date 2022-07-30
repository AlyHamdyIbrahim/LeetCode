class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        r_len = len(grid)
        c_len = len(grid[0])
        perimeter = 0
        for r in range(r_len):
            for c in range(c_len):
                perimeter += self.explore(self, grid, r, c)
        return perimeter

    def explore(self, grid, r, c):
        if not self.land(self, grid, r, c):
            return 0
        perimeter = 4
        if self.land(self, grid, r-1, c):
            perimeter -= 1
        if self.land(self, grid, r+1, c):
            perimeter -= 1
        if self.land(self, grid, r, c-1):
            perimeter -= 1
        if self.land(self, grid, r, c+1):
            perimeter -= 1

        return perimeter

    def land(self, grid, r, c):
        r_inbounds = 0 <= r < len(grid)
        c_inbounds = 0 <= c < len(grid[0])
        if not r_inbounds or not c_inbounds or grid[r][c] == 0:
            return False
        return True
