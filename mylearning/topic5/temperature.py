maxx = float(input("Temp: "))
month = 1
for i in range(2,13):
    temp = float(input("Temp: "))
    if temp > maxx:
        maxx = temp
        month = i
print("max temp = %.1f in %d month"%(maxx,month))
    
