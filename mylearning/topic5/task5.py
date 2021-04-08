counter = 0
for i in range(1,11):
    num = int(input("Input the number %d more then 2: " % i))
    if num % 5 == 0:
        counter += 1
print("Number of multiples of 5: ",counter)
        
