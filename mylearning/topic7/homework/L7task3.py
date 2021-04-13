def square(side_func):
    from math import sqrt
    list_Square = [side_func*4,side_func**2,side_func*sqrt(2)]
    return list_Square
def main():
    print("If you want to exit input(0)!!!")
    while True:
        side = int(input("Input the side of square: "))
        if side == 0:
            print("The end")
            break
        list_square = square(side)
        print("Perimeter of square: ",list_square[0])
        print("Square of area: ",list_square[1])
        print("Diagonal of square: %.2f"%list_square[2])

if __name__ == "__main__":
    main()
    
   
