year = int(input("Input year: "))
if year % 4 != 0:
    print("Year is simple.")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Year is high")
    else:
        print("Year is simple.")
else:
    print("Year is high")
year //= 100
year += 1
print("The year belongs to the %d century" % (year))
    
        
    
