import random
rows = int(input("Input matrix number of rows: "))
columns = int(input("Input matrix number of columns: "))
matrix = [[random.randint(0,999)for j in range(0,columns)]for i in range(0,rows)]
list_two_digit = []
counter = 0
print("original matrix:")
for i in range(0,rows):
    for j in range(0,columns):
        print("%4d"%matrix[i][j],end = "")
    print()
for i in range(0,rows):
    for j in range(0,columns):
        num = matrix[i][j]
        num = str(num)
        if len(num) == 2:
            counter +=1
            list_two_digit.append(int(num))
print("Number of items with two digits: ",counter)
print("Numbers with two digits: ",list_two_digit)
            
            
    

    
