class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        # create prefix sum for each row considering only the row
        self.prefix = []
        for row in matrix:
            prefix_row = []
            total = 0
            for col in row:
                total += col
                prefix_row.append(total)
            self.prefix.append(prefix_row)
        print(self.prefix)
                
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # get the sum of the first row disregarding unnecessary left and right values
        row_1_right_sum = self.prefix[row1][col2]
        row_1_left_sum = self.prefix[row1][col1-1] if col1 > 0 else 0
        row_1_result = row_1_right_sum - row_1_left_sum

        # get the sum of the second row disregarding unnecessary left and right values
        if row2 != row1:
            row_2_right_sum = self.prefix[row2][col2]
            row_2_left_sum = self.prefix[row2][col1-1] if col1 > 0 else 0
            row_2_result = row_2_right_sum - row_2_left_sum
        else:
            # if is the same row we already got the value from row 1
            row_2_result = 0

        if row2 - row1 == 1:
            # if its only 2 rows
            return row_1_result + row_2_result
        else:
            # get the sum of the middle rows disregarding unnecessary left and right values
            middle_row_sum = 0
            for row in range(row1+1, row2):
                middle_row_right_sum = self.prefix[row][col2]
                middle_row_left_sum = self.prefix[row][col1-1] if col1 > 0 else 0
                middle_row_sum += middle_row_right_sum - middle_row_left_sum
            
            return middle_row_sum + row_1_result + row_2_result




matrix = NumMatrix([[-1]])
print([[-1]])
print(matrix.sumRegion(0,0,0,0))


matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(matrix.sumRegion(1,2,2,4))
print(matrix.sumRegion(2,1,4,3))