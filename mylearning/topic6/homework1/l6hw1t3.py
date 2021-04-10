from random import randint
list_num = []
counter_positive = 0
counter_negative = 0
counter_zero = 0
for i in range(0,20):
    num = randint(-5,4)
    list_num.append(num)
    if num > 0:
        counter_positive += 1   
    elif num < 0:
        counter_negative += 1   
    elif num == 0:
        counter_zero += 1   
print("List: ",list_num)
print("counter_positive: ",counter_positive)
print("counter_negative: ",counter_negative)
print("counter_zero: ",counter_zero)
