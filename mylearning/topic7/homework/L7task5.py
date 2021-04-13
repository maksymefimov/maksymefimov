def bank(bank_money,bank_years):
    bank_percent = bank_money
    for i in range(0, bank_years):
        bank_percent = bank_percent * 0.1 + bank_percent

    return bank_percent
    
def main():
    print("If you want to exit input(0)!!!")
    while True:
        user_money = int(input("Input the amount of money:"))
        user_year = int(input("Input the amount of years:"))                 
        if user_money == 0 or user_year == 0:
            print("The end")
            break
        print("Money after %d years on deposit: %d$"%(user_year,\
                                                  bank(user_money,user_year)))

if __name__ == "__main__":
    main()
    
   
