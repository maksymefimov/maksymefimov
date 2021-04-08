a = int(input("A: "))
b = int(input("B: "))
counter = 0
if a > b:
    a,b = b,a
if a%2 == 0:
    a += 1


for i in range(a,b,2):
    counter += i
if b%2==1:
    counter += b
print("counter = %d" %(counter))
