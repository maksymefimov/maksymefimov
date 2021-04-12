list_month = ["","January","February","March","April","May","June","July",\
              "August","September","October","November","December"]
month = 1
max_temp = float(input("Input Temperature in %s: "%list_month[month]))
for i in range(2,13):
    temp = float(input("Input Temperature in %s: "%list_month[i]))
    if temp > max_temp:
        max_temp = temp
        month = i
print("Max. temperature = %.1f in %s month"%(max_temp,list_month[month]))
    
