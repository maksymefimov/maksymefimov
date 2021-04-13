def is_year_leap(year_func):
    if year_func % 4 != 0:
        return("Year is simple.")
    elif year_func % 100 == 0:
        if year_func % 400 == 0:
            return("Year is high")
        else:
            return("Year is simple.")
    else:
        return("Year is high")
def main():
    while True:
        year = int(input("Input year(if you want to exit input(0)): "))
        if year == 0:
            print("The end")
            break
        print(is_year_leap(year))

if __name__ == "__main__":
    main()
    
   
