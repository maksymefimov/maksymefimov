import random
n = int(input("input n: "))
numbers = []
print("our list: ")
for i in range(n):
    numbers.append(random.randint(1,10))
    print("%d, "%numbers[i], end="")
print()
print("unique elements")
for item in numbers:
    if numbers.count(item) == 1:
       print(item)
