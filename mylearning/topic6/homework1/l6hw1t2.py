list1 = []
pro_num = 1
sum_num = 0
for i in range(1,11):
    num = float(input("Input the number %d for list: "%i))
    list1.append(num)
for i in range(len(list1)):
    sum_num +=list1[i]
    pro_num *=list1[i]
print("List 1  :",list1)
print("Product :",pro_num)
print("Sum     :",sum_num)    
    
    
