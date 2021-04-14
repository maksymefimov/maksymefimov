list_general = input("Input a random set of numbers, letters, symbols: ")
list_general = list(list_general)
print(list_general)
list_num =[]
list_let =[]
list_sign = list(list_general)
for i in list_general:
    for let in range (65,91):
        if chr(let) == i:
            list_let.append(i)
            list_sign.remove(i)
    for let in range (97,123):
        if chr(let) == i:
            list_let.append(i)
            list_sign.remove(i)
    for num in range (48,57):
        if chr(num) == i:
            list_num.append(i)
            list_sign.remove(i)
print("Letters: ",list_let)
print("Numbers: ",list_num)
print("Sign: ",list_sign)
list_num = tuple(list_num)
list_let = tuple(list_let)
list_sign = tuple(list_sign)
test = input("Input  number or letter or symbol: ")
if test in list_num:
    print("Index in tuple numbers: %d "%(list_num.index(test)))
elif test in list_let:
    print("Index in tuple letters: %d "%(list_let.index(test)))
elif test in list_sign:
    print("Index in tuple numbers: %d "%(list_sign.index(test)))
else:
    print("Unknown object!!!")
print("Reverse letters:",list_let[::-1])


        
    
