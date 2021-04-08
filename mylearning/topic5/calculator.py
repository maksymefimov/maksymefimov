#повідомити користувача про умови обчислень
print ("hello i m calculator")
print("You_ve to input operation sign: +,-,*,/")
print("Input 0 to stop!")
sign = input("Input sign please: ")
while sign not in '0+-*/ ':
        sign = input("Input sign please: ")
#цикл для введення операцій
while sign != '0':
    #перевірка яка дія та її виконання
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    if sign=='+':
        print("sum= %d"%(a+b))
    elif sign=='-':
        print("sub= %d"%(a-b))
    elif sign=='*':
        print("mult= %d"%(a*b))
    else:
        if b == 0:
            print("error")
        else:
            print("div= %.2f"%(a/b))
    sign = input("Input sign please: ")
    while sign not in '0+-*/ ':
        sign = input("Input sign please: ")
    
        
        






