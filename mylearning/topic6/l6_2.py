import random
n = int(input("Input N"))
numbers = []
print("Our list: ")
for i in range(n):
    numbers.append(random.randint(1,100))
    print("%d, "%numbers[i],end = "")
position = int(input("Quant of positions"))
direction = input("left or right L/R:")
if direction.upper() == 'L':
    new_numbers = numbers[position:]+numbers[:position]
else:
    new_numbers = [0] * position + numbers
print("Our list: ")
for item in new_numbers:
    print("%d, "%item,end = "")
print()
    
