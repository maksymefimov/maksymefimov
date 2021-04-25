def arithmetic(num1,num2,sign):
    if sign == "+":
        return(num1 + num2)
    elif sign == "-":
        return(num1 - num2)
    elif sign == "*":
        return(num1 * num2)
    elif sign == "/":
        return(num1 / num2)
    else:
        return("Unknown operation!!!")
def main():
    while True:
        numm1 = float(input("Input first number: "))
        numm2 = float(input("Input Second number: "))
        sign1 = input("Input sign(if you want to exit input(0)): ")
        if sign1 == '0':
            print("The end")
            break
        print(arithmetic(numm1,numm2,sign1))

if __name__ == "__main__":
    main()
    
   
