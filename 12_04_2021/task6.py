counter = 1
positive = 0
negative = 0 
while counter != 0:
    num = int(input("Input number:"))
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        break
    procent100 = 100 / (positive + negative)
    procent_positive = procent100 * positive
    procent_negative = procent100 * negative
    print("Percentage of positive numbers: %d%%" % procent_positive)
    print("Percentage of positive numbers: %d%%" % procent_negative)
print("The End")    
       
