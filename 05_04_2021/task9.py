x = int(input("Enter the amount of money($): "))
x1 = x // 200
x2 = x1 * 200
x3 = x - x2
print(x1,"-200$")
if x3 >=100:
    x4 = x3 // 100
    x5 = x4 * 100
    x6 = x3 - x5
    print(x4,"-100$")
    if x6 >= 10:
        x7 = x6 // 10
        x8 = x7 * 10
        x9 = x6 - x8
        print(x7,"-10$")
        if x9 >= 1:
            print(x9,"-1$")
    elif x6 < 10:
        print(x6,"-1$")
elif x3 < 100:
    x11 = x3 // 10
    x12 = x11 * 10
    x13 = x3 - x12
    print(x11,"-10$")
    if x13 >= 1:
        print(x13,"-1$")



        
        
        
        
        
    


