matrix_1 = [ [0]*5 for i in range(4) ]
for i in range(4):
    for j in range(4):
        matrix_1[i][j] = int(input("Input the number: "))
    matrix_1[i][4] = sum(matrix_1[i])
print("Matrix_1:")
for i in range(4):
    for j in range(5):
        print("%4d"%matrix_1[i][j],end = "")
    print()
