from random import randint
matrix = [[randint(0,9) for j in range(10)] for i in range(10)]
print("Original matrix:")
for i in range(10):
    for j in range(10):
        print("%4d"%matrix[i][j], end = '')
    print()
counter_1 = 0
counter_2 = 5
for item in matrix:
    if counter_1 < 5:
        temp = item[counter_1]
        item[counter_1] = item[(counter_1+1)*-1]
        item[(counter_1+1)*-1] = temp
        counter_1 +=1
    else:
        counter_2 -=1 
        temp = item[counter_2]
        item[counter_2] = item[(counter_2+1)*-1]
        item[(counter_2+1)*-1] = temp   
print("changed matrix:")
for i in range(10):
    for j in range(10):
        print("%4d"%matrix[i][j], end = '')
    print()
