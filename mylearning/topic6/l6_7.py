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
