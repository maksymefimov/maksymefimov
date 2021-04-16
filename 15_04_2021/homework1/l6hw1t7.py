from random import randint
list_num = []
items = int(input("Input number of items: "))
for i in range(items):
    list_num.append(randint(-100,100))
print("Original list: ",list_num)
temp = list_num[list_num.index(min(list_num))]
list_num[list_num.index(min(list_num))] = list_num[list_num.index(max(list_num))]
list_num[list_num.index(max(list_num))] = temp
print("Changed list: ",list_num)


                    
