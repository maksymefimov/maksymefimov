list_month = ["","January","February","March","April","May","June","July",\
              "August","September","October","November","December"]
month = 1
maxx = float(input("Input Temperature in %s: "%list_month[month]))
for i in range(2,13):
    temp = float(input("Input Temperature in %s: "%list_month[i]))
    if temp > maxx:
        maxx = temp
        month = i
print("max temp = %.1f in %s month"%(maxx,list_month[month]))
    
