from random import randint
list1 = []
list2 = []
list3 = []
for i in range(1,6):
    list1.append(randint(0,100))
    num = int(input("Input the number %d for list: "%i))
    list2.append(num)
    list3.append(list1[i-1]+list2[i-1])
print("List 1:",list1)
print("List 2:",list2)
print("Sum   :",list3)    
    
    
