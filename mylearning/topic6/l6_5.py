import random
n = int(input("input n: "))
numbers = []
print("our list: ")
for i in range(n):
    numbers.append(random.randint(1,10))
    print("%2d, "%numbers[i], end="")
print()
number_counts = []
i = 0
for item in numbers:
    number_counts.append(numbers.count(item))
    print("%2d, "%number_counts[i], end="")
    i += 1
print()
print("max counts: %2d" %numbers[number_counts.index(max(number_counts))])
