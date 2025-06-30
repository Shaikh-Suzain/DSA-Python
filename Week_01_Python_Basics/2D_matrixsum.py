matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total=0
for row in matrix:
    total+=sum(row)
print("Total sum:", total)


#enumerate(matrix) loops through each row and gives you the index (i).
for i, row in enumerate(matrix):
    print(f"Sum of row {i+1}:", sum(row))
    
for col in range(3):
    col_sum = matrix[0][col] + matrix[1][col] + matrix[2][col]
    print(f"Sum of column {col+1}:", col_sum)


# enumerate
# What: Adds an automatic counter (index) while looping through an iterable (like a list, tuple, string).

# Use case: When you want both the index and the item at the same time.

# 📌 range
# What: Generates a sequence of numbers.

