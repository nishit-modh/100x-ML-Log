# 9. MATRIX TRANSPOSE
# Problem: Convert a 2D list (matrix) such that rows become columns.
# Example: matrix =
# [[1, 2, 3],
#  [4, 5, 6]] ->
#  Output:
# [[1, 4],
#  [2, 5],
#  [3, 6]]

#=========================================
# 1st attempt - correct logic
#=========================================
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = []

for j in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[j])
    transpose.append(transposed_row)
print(transpose)

matrix = [[1, 2, 3], [4, 5, 6]]


#=========================================
# pythonic one-liner for same logic
#=========================================
# THE ONE-LINER DECONSTRUCTED:
# 1. The outer brackets [ ... for j in range(len(matrix[0])) ] 
#    create the main list. It says: "Run this loop for every column index (0, 1, 2)."
# 
# 2. Inside, we have ANOTHER list comprehension: [row[j] for row in matrix]
#    This is the "result" that gets put into the main list. 
#    It says: "For the current column j, go through every row and grab the j-th item."

transpose = [[row[j] for row in matrix] for j in range(len(matrix[0]))]

# Logic Trace:
# j=0: [row[0] for row in matrix] -> grabs 1 from row1, 4 from row2 -> [1, 4]
# j=1: [row[1] for row in matrix] -> grabs 2 from row1, 5 from row2 -> [2, 5]
# j=2: [row[2] for row in matrix] -> grabs 3 from row1, 6 from row2 -> [3, 6]

print(transpose) # [[1, 4], [2, 5], [3, 6]]