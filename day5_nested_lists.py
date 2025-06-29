matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


print(matrix)
print("Middle element:",matrix[1][1])

for row in matrix:
    for value in row:
        print(value,end=" ")
        
    print()