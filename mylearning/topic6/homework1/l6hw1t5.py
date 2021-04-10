from random import randint
n = int(input("Input number of items: "))
list_num = []
list_index = []
for i in range (0,n):
    list_num.append(randint(-100,100))
print("List:",list_num)
i = 0
while i < n:
    if list_num[i] < 0:
        list_num.pop(i)
        i -= 1
        n -= 1
    i += 1
print("List without negative numbers:",list_num)
for i in range(len(list_num)):
    if list_num[i] % 2 == 0:
        list_index.append(i)
print("Indexes with even numbers: ",list_index)
