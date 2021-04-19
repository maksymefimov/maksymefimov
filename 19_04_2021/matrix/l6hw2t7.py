from random import randint
matrix = [[randint(0,99) for j in range(5)] for i in range(5)]
print(type(matrix))
print("Original matrix:")
for i in range(5):
    for j in range(5):
        print("%4d"%matrix[i][j], end = '')
    print()
counter = 4
while counter > 0:
    verification = 0
    for j in range(counter+1):
        if matrix[0][j] > matrix[0][verification]:
            verification = j
    for i in range(5):
        temp = matrix[i][verification]
        matrix[i][verification] = matrix[i][counter]
        matrix[i][counter] = temp
    counter -= 1
print("Original matrix:")   
for i in range(5):
    for j in range(5):
        print("%4d"%matrix[i][j], end = '')
    print()



