import random
list_min= []
num_col = []
matrix = [[random.randint(0,100)for j in range(5)]for i in range(5)]
for i in range(5):
    for j in range(5):
        print("%4d"%matrix[i][j],end="")
    print()
for j in range(5):
    for i in range(5):
        num = matrix[i][j]  
        list_min.append(int(num))
    num_col.append(min(list_min))
    list_min.clear()
print("List of minimal numbers in columns:\n",num_col)
print("Max. number in minimal numbers in columns:",max(num_col))
    
