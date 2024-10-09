matrix = [[1,2,3], [4,5,6], [7,8,9]]

prefix_rows = []
prefix_columns = []
for r_idx, row in enumerate(matrix):
    prefix_row = []
    prefix_col = [None]*len(row)
    total_row = 0
    total_column = 0
    for c_idx, col in enumerate(row):
        total_row += col
        prefix_col[r_idx] += col
        prefix_row.append(total_row)
    prefix_rows.append(prefix_row)
    prefix_columns.append(prefix_col)

print(prefix_rows)
print(prefix_columns)