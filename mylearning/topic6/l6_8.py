import random
m = int(input("input M: "))
n = int(input("input N: "))
numbers = [[0] * n] * m
print("our list: ")
for i in range(m):
    for j in range(n):
        numbers[i][j] =(random.randint(1,10))
        print("%4d, "%numbers[i][j], end="")
    print()
temp1 = []
for j in range(n):
    temp1.append(numbers[2][j]) #3rd row
print("min of 3rd row : %4d"%min(temp1))
temp1 = []
for i in range(m):
    temp1.append(numbers[i][1]) #2nd column
print("max of 2nd column : %4d"%max(temp1))
    
