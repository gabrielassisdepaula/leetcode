# Best Runtime: 970ms
# Beats: 94.88%

# Best Memory: 27.19mb
# Beats: 83.33%

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        # add padding zeros to the matrix for edge cases
        self.prefix_sum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for row in range(ROWS):
            row_prefix_sum = 0
            for col in range(COLS):
                # calculate the ONLY the row prefix sum, disregarding column sums
                row_prefix_sum += matrix[row][col]
                # sum row_prefix_sum with all the above values up to that column, accounting for padding zeros
                self.prefix_sum[row+1][col+1] = row_prefix_sum + self.prefix_sum[row][col+1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # bottom_right - above - left + top_left
        return self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row1][col2+1] - self.prefix_sum[row2+1][col1] + self.prefix_sum[row1][col1]