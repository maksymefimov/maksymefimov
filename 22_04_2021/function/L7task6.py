def is_prime(num):
    if num in list_simple_number:
        return True
    else:
        return False
def main():
    numbers = 1000
    global list_simple_number
    list_simple_number = []
    counter_del = 0
    for i in range(2, numbers+1):
        for j in range(2, i):
            if i % j == 0:
                counter_del += 1
        if counter_del == 0:
            list_simple_number.append(i)
        else:
            counter_del = 0
    print(list_simple_number)
    print("If you want to exit input(0)!!!")
    while True:
        number = int(input("Input the number from 0 to 1000: "))
        print(is_prime(number))
        if number == 0:
            print("The end")
            break
if __name__ == "__main__":
    main()
