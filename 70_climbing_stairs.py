class Solution:
    # Iterative approach
    def climbStairs(self, n: int) -> int:
        x, y = 1, 1
        for _ in range(n-1):
            x, y = y, x + y
        return y

    # Recursive approach
    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs2(n - 1) + self.climbStairs2(n - 2)
