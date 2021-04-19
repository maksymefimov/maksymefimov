from random import randint
matrix = [[randint(0,99) for j in range(5)] for i in range(5)]

print("Original matrix:")
for i in range(5):
    for j in range(5):
        print("%4d"%matrix[i][j], end = '')
    print()
counter_1 = 0 
while counter_1 < 5:
    counter_2 = 0
    for j in range(counter_1+1):
        if matrix[0][j] > matrix[0][counter_2]:
            counte_2 = j
    for i in range(5):
        m = matrix[i][counter_2]
        matrix[i][counter_2] = matrix[i][counter_1]
        matrix[i][counter_1] = m
    counter_1 += 1
print("Original matrix:")   
for i in range(5):
    for j in range(5):
        print("%4d"%matrix[i][j], end = '')
    print()



