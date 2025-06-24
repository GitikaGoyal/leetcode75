class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        freq = defaultdict(int)
        n = len(grid)
        count = 0

        # Count frequency of each row (as a tuple)
        for row in grid:
            freq[tuple(row)] += 1

        # For each column, build the tuple and check frequency
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += freq[col]

        return count
