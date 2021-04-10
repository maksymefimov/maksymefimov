import random
n = int(input("input n: "))
numbers = []
print("our list: ")
for i in range(n):
    numbers.append(random.randint(1,10))
    print("%d, "%numbers[i], end="")
print()
print("Our new list:" )
min_elem = min(numbers)
max_elem = max(numbers)
temp = numbers[numbers.index(min_elem)]
numbers[numbers.index(min_elem)] = numbers[numbers.index(max_elem)]
numbers[numbers.index(max_elem)] = temp
for item in numbers:
    print("%d, "%item, end ="")
print()
