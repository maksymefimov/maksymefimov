tup = (1,2,3,5,7,3,6,9,0,2,-4,-7,-8)
print("Original tup:\n",tup)
list_tup = sorted (tup)
tup = tuple(list_tup)
print("Sorted tup:\n",tup)
tup = (1,2,3,5,7,3,6,9,0,2,-4,-7,-8)
tup = tuple(sorted (tup))
print("Sorted tup:\n",tup)
##----------------------------------
grades=[("Ann", 4), ("Bob", 2), ("Elizabeth", 3), ("Dan", 5)] 
for item in grades:
    print("hello, %s! Your grade is %d!" % (item[0],item[1]))
##----------------------------------
names=("Ann", "Bob", "Elizabeth", "Mr. McMullen", "Mrs. Smith")
for item in names:
    if '.' in item:
        
        print("Good morning %s!"%(item))
    else:
        print("Hello, %s!" % (item))
        



