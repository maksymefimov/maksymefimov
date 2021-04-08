counter = 0
a = int(input("Input A: "))
b = int(input("Input B: "))
if a > b:
    a,b=b,a
if a % 2 == 0:
    x = a
else:
    x = a + 1

while x <=b:
    counter += 1
    x += 2
print("The number od odd: %2d"%(counter))
#print("The end")    
 
