#1----------------------------------------------
import random
n = int(input("Input number of items in list:"))
numbers = []
print("Original list: ")
for i in range(n):
    numbers.append(random.randint(1,100))
    print("%d, "%numbers[i],end = "")
print()
position = int(input("Quant of positions: "))
direction = input("Left or right L/R:")
print("Modified list: ")
for i in range(0,position):
    if direction.upper() == 'L':
        numbers = numbers + [0]
        print(numbers)
    elif direction.upper() == 'R':
        numbers = [0] + numbers 
        print(numbers)
    else:
        print("Unknown!!!")
        break
#2-----------------------------------------------
n = int(input("Input number of items in list: "))
numbers = []
print("Original list: ")
for i in range(n):
    numbers.append(random.randint(1,100))
    print("%d, "%numbers[i], end="")
print()
print("Max.item = %d Index.item = %d"%(max(numbers),numbers.index(max(numbers))))
