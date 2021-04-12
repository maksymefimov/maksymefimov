
def sum_string(str_numbers):
    list_numbers = str_numbers.split()
    sum_numbers = 0
    for item in list_numbers:
        sum_numbers += int(item)
    return sum_numbers
def main():
    print("Our program will count the sum of numbers")
    print("press # to stop the process")
    sum_total = 0
    while True:
        str_numbers = input("Input numbers throught space and press Enter: ")
        if '#' in str_numbers:
            sum_total += sum_string(str_numbers[:str_numbers.index('#')])
            break
        sum_total += sum_string(str_numbers)
    print("Total sum = %d "%sum_total)
if __name__ == "__main__":
    main()
