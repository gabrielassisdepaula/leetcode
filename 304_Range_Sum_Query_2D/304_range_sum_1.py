# https://www.youtube.com/watch?v=WibxoqMSMCw
# Best Runtime: 1004ms
# Beats: 52.72%

# Best Memory: 26.98b
# Beats: 95.33%

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows, cols = len(matrix), len(matrix[0])
        # Create matrix of the same size but with added padding zeros on the left and top side
        self.prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        # iterate the rows skipping the padding zeros on the top
        for row in range(1, rows + 1):
            # iterate the columns skipping the padding zeros on the left
            for col in range(1, cols + 1):
                # adjacent_left = self.prefix_sum[row-1][col]
                # adjacent_top = self.prefix_sum[row][col-1]
                # adjacent_left_up_diagonal = self.prefix_sum[row-1][col-1]
                # current_matrix_value = matrix[row-1][col-1]

                # we subtract the adjacent_left_up_diagonal because we added it twice, once for the previous row and again for the current row
                # self.prefix_sum[row][col] = adjacent_left + adjacent_top - adjacent_left_up_diagonal + current_matrix_value

                # adjacent left + adjacent top - adjacent left up diagonal + current matrix value
                self.prefix_sum[row][col] = self.prefix_sum[row-1][col] + self.prefix_sum[row][col-1] - self.prefix_sum[row-1][col-1] + matrix[row-1][col-1]
    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # +1 to account for padding and get the correct position
        # bottom_right_corner_sum = self.prefix_sum[row2+1][col2+1]

        # row1 already gets the adjacent position because of padding
        # col2+1 to get the right column because of padding 
        # adjacent_top_right_corner_sum = self.prefix_sum[row1][col2+1]

        # row2+1 to account for padding
        # col1 already gets the adjacent left value because of padding
        # adjacent_left_bottom_corner_sum = self.prefix_sum[row2+1][col1]

        # row1 and col1 already gets the adjacent top left value because of padding
        # adjacent_diagonal_top_corner_sum = self.prefix_sum[row1][col1]

        # adjacent_top_right_corner and adjacent_left_bottom_corner subtracts adjacent_diagonal_top_corner twice
        # that's why we add its value, it should be subtracted only once!
        # return bottom_right_corner_sum - adjacent_top_right_corner_sum - adjacent_left_bottom_corner_sum + adjacent_diagonal_top_corner_sum

         
        return self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row1][col2+1] - self.prefix_sum[row2+1][col1] + self.prefix_sum[row1][col1]




matrix = NumMatrix([[-1]])
print([[-1]])
print(matrix.sumRegion(0,0,0,0))


matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(matrix.sumRegion(1,2,2,4))
print(matrix.sumRegion(2,1,4,3))