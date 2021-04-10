from random import randint
list_num = []
items = int(input("Input number of items: "))
for i in range(0,items):
    list_num.append(randint(-100,100))
print("Original list: ",list_num)
min_num = min(list_num)
max_num = max(list_num)
temp = list_num[list_num.index(min_num)]
list_num[list_num.index(min_num)] = list_num[list_num.index(max_num)]
list_num[list_num.index(max_num)] = temp
print("Changed list: ",list_num)


                    
