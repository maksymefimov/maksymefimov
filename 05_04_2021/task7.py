number = int(input("Input number from -99 to 99: "))
if number > 0:
    if number > 0 and number < 10:
        print("This is positive one-digit number")
    elif number > 9 and number < 100:
        print("This is positive two-digit number")
    else:
        print("Unknmown number")
elif number < 0:
    if number < 0 and number > -10:
        print("This is negative one-digit number")
    elif number < -9 and number > -100:
        print("This is negative two-digit number")
    else:
        print("Unknmown number")
