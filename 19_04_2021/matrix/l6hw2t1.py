import random
rows = int(input("Input matrix number of rows: "))
columns = int(input("Input matrix number of columns: "))
matrix = [[random.randint(1,10)for j in range(0,columns)]for i in range(0,rows)]
list_num = []
list_sum = []
print("original matrix:")
for i in range(0,rows):
    for j in range(0,columns):
        print("%4d"%matrix[i][j],end = "")
    print()
for i in range (0,rows):
    num = sum(matrix[i])
    matrix[i].append(num)
for j in range (0,columns+1):
    for i in range (0,rows):
        list_num.append(matrix[i][j])
        if i == rows -1:
            num = sum(list_num)
            list_sum.append(num)
            list_num.clear()
matrix.append(list_sum)
print("Modified matrix:")
for i in range (0,rows+1):
    for j in range (0,columns+1):
        print("%4d " % matrix[i][j], end = "")
    print()
print
