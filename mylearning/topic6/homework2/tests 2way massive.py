a = [[1,2,3],[4,5,6],[7,8,9]]
list_num = []
list_sum = []
for i in range (0,3):
    print(a[i])
for i in range (0,3):
    num = sum(a[i])
    a[i].append(num)
for j in range (0,3+1):
    for i in range (0,3):
        list_num.append(a[i][j])
        if i == 2:
            num = sum(list_num)
            list_sum.append(num)
            list_num.clear()
a.append(list_sum)      
for i in range (0,3+1):
    for j in range (0,3+1):
        print("%4d "%a[i][j], end = "")
    print()
