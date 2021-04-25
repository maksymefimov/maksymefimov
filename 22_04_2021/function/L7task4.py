def season(month):
    if month == 12 or month in range(1,3):
        return "Winter"
    if month in range(3,6):
        return "Spring"
    if month in range(6,9):
        return "Summer"
    if month in range(9,12):
        return "Autumn"
def main():
    print("If you want to exit input(0)!!!")
    while True:
        month_n = int(input("Input the number of month: "))
        if month_n == 0:
            print("The end")
            break
        print("Season of month is %s!"%season(month_n))

if __name__ == "__main__":
    main()
    
   
