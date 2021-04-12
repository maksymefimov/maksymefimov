import random
p = random.randint(0,100)
h = random.randint(0,100)
sum_p = 0
dob_h = 1
counter_ph = 0
if p > h:
    p,h = h,p
print("P = %d\nH = %d" % (p,h))
while True:
    num = int(input("Input the number: " ))
    if num < p:
        sum_p += num
    elif num > h:
        dob_h *= num 
    elif p < num < h:
        counter_ph += 1
    else:
       break
if dob_h == 1:
    dob_h = 0
print("The sum of numbers is less than P: %5d" % sum_p)
print("The product of numbers greater than H: %d" % dob_h)
print("The number of numbers between P and H: %1d" % counter_ph)    
