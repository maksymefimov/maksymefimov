number = int(input("Enter the number of your seat on the train: "))
number_mod = number % 2
if 1 > number or number > 54:
    print("Unknown number.")
elif number_mod == 0:
    print("Your place on top.")
elif number_mod > 0:
    print("Your place at the bottom.")
if number < 37 and number > 0 :
    print("In the compartment.")
elif number > 36 and number < 55:
    print("From the side.")
        
        
             
             
