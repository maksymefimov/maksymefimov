cheesePizza = {"Creamy Garlic Parmesan Sauce", "Cheese", "Toasted Parmesan"}
print(cheesePizza)
print(type(cheesePizza))

##set not index---------------
transport_set1 = set(['boat', 'bus', 'plane', 'train'])
person_set2 = set(('cyclist', 'driver', 'pedestrian'))
print(transport_set1)
print(person_set2)
##--------------------------------------------
symbol = set()
for symb in range (97,123):
    symbol.add(chr(symb))
for symb in sorted(symbol):
    print("%s,"%symb ,end = "")
    
##---------------------------------------------
vow = ('a','o','e','i','y','u')
numb = set()
for i in range(10):
    numb.add(chr(i))

my_str = input("input string:")
count_v = 0
count_n = 0
count_s = 0
count_k = 0
for symb in my_str:
    if symb in vow:
        count_v += 1
    elif symb in numb:
        count_n += 1
    elif symb in ".,;:!^":
        count_s += 1
    else:
        count_k +=1
if count_k > count_v :
    
    print("Consonants more")
else:
    print("Vowels more")
    
