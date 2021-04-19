matrix_1 = [ [0]*3 for i in range(3) ]
matrix_2 = [ [0]*3 for i in range(3) ]
matrix_3 = [ [0]*3 for i in range(3) ]
list_max = []
for i in range(1,4):
    for j in range(1,4):
        matrix_1[i-1][j-1] = int(input("Input the number of %d row and %d column(Matrix_1): "%(i,j)))
for i in range(1,4):
    for j in range(1,4):
        matrix_2[i-1][j-1] = int(input("Input the number of %d row and %d column(Matrix_2): "%(i,j)))
    
print("Matrix_1:")
for i in range(0,3):
    for j in range(0,3):
        print("%4d"%matrix_1[i][j],end = "")
    print()
print("Matrix_2:")
for i in range(0,3):
    for j in range(0,3):
        print("%4d"%matrix_2[i][j],end = "")
    print()
print("Matrix_3 :")
for i in range(0,3):
    for j in range(0,3):
        list_max.append(matrix_1[i][j])
        list_max.append(matrix_2[i][j])
        matrix_3 [i][j] =(max(list_max))
        list_max.clear()
        print("%4d"%matrix_3[i][j],end = "")
    print()
    
