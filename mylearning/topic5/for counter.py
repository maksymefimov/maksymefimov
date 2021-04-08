##for j in ['mango','apple','raspberry','peach','plum']:
##    print("I like: %s"%(j))
a = int(input("left: "))
b = int(input("right: "))
step = int(input("Step: "))
for j in range(a,b+1,step):
    print("Do: %d"%(j))
