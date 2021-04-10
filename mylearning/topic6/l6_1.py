import random
n = int(input("Input N"))
numbers = []
print("Our list: ")
for i in range(n):
    numbers.append(random.randint(1,100))
    print("%d, "%numbers[i],end = "")
print("\nMax element = %d"%max(numbers))
    
