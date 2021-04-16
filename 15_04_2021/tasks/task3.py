#1.-----------------------------------------------
import random
n = int(input("Input number of items in list: "))
numbers = []
print("Original list: ")
for i in range(n):
    numbers.append(random.randint(1,10))
    print("%d, "%numbers[i], end="")
print()
print("Unique elements")
for item in numbers:
    if numbers.count(item) == 1:
       print("%d, "%item, end = "")
print()
print()
#2.------------------------------------------------
numbers1 = []
print("Original list: ")
for i in range(n):
    numbers1.append(random.randint(1,100))
    print("%d, "%numbers1[i], end="")
print()
print("Changed list(Min/Max): ")
min_elem = min(numbers1)
max_elem = max(numbers1)
temp = numbers1[numbers1.index(min_elem)]
numbers1[numbers1.index(min_elem)] = numbers1[numbers1.index(max_elem)]
numbers1[numbers1.index(max_elem)] = temp
for i in range(n):
    print("%d, "%numbers1[i], end="")
print()
print()
#3.-------------------------------------------------
print("Original list: ")
numbers2 = []
for i in range(n):
    numbers2.append(random.randint(1,10))
    print("%d, "%numbers2[i], end="")
print()
number_counts = []
i = 0
for item in numbers2:
    number_counts.append(numbers2.count(item))
    print("%d, "%number_counts[i], end="")
    i += 1
print()
print("Max counts number: %2d" %numbers2[number_counts.index(max(number_counts))])

