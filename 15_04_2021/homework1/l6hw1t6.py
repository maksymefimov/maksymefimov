from random import randint
list_num = []
list_num_uniq = []
items = int(input("Enter number of items: "))
for i in range(0,items):
      list_num.append(randint(1,10))
print(list_num)
for item in list_num:
    if list_num.count(item) == 1:
        list_num_uniq.append(item)
print("Numbers that occur once: ",list_num_uniq)
