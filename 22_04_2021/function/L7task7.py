def date(date_info):
    month_H = {1, 3, 5, 7, 8, 10, 12}
    month_L = {4, 6, 9, 11}
    if date_info[1] <= 12 and 1 <= date_info[0] <= 31:
        if date_info[1] in month_H and date_info[0] <= 31:
            result = True
        elif date_info[1] in month_L and date_info[0] <=30:
            result = True
        elif date_info[1] == 2 and (date_info[0] <= 29):
            if (date_info[0] == 29) and not ((date_info[2] % 4 == 0) and (date_info[2] % 100 != 0) or (date_info[2] % 400 == 0)):
                result = False
            else:
                result = True
        else:
            result = False
    else:
        result = False
    return(result)
def main():
    print("If you want to exit input(0)!!!")
    while True:
        date_input = input("Input date in format(day,month,year): ")
        if date_input == '0':
            print("The end")
            break
        date_input = date_input.split(',')
        for i in range(0,3):
            date_input[i] = int(date_input[i])
        print(date_input)
        if len(date_input) > 3:
            print("Unknown format of date!!!",date_input)
        else:
            print(date(date_input))
        
if __name__ == "__main__":
    main()

    
