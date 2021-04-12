
def square_figure(str_numbers):
    list_numbers = str_numbers.split()
    for item in range(len(list_numbers)):
        list_numbers[item] = float(list_numbers[item])
    if len(list_numbers) == 1:
       return 3.14*list_numbers[0]**2
    if len(list_numbers) == 2:
       return list_numbers[0]*list_numbers[1]
    if len(list_numbers) == 3:
       p = 0
       for item in list_numbers:
           p += item
       p = p / 2
       s = 1
       for item in list_numbers:
           s *= (p-item)
       s *= p
       return s ** 0.5
def main():
    print("Our program will count the square of figure")
    str_numbers = input("Input numbers throught space and press Enter: ")
    print("Square = %5.2f  "%square_figure(str_numbers))
if __name__ == "__main__":
    main()
