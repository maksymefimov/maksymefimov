def season(month):
    list_month = ["not available","January","February","March","April","May","June","July",\
              "August","September","October","November","December"]
    if 0< month and month < 13:
        return list_month[month]
    return list_month[0]
    
def main():
    print("If you want to exit input(0)!!!")
    while True:
        month_n = int(input("Input the number of month: "))
        if month_n == 0:
            print("The end")
            break
        print("Name of month is %s!"%season(month_n))

if __name__ == "__main__":
    main()
    
   
