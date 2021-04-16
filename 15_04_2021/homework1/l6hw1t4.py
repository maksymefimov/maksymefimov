from random import randint
list_positive = []
list_negative = []
list_bank = []
for i in range(0,10):
    num = randint(-5,5)
    list_bank.append(num)
    if num > 0:
        list_positive.append(num)
    if num < 0:
        list_negative.append(num)
        
print("List: ",list_bank)
print("List positive: ",list_positive)
print("List negative: ",list_negative)    
    
    

