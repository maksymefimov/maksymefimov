def NSD(a, b):
    """Max common divizer"""
    while a != b:
        if a < b:
           b = b - a
        else:
           a = a - b
    return a
def NSK(a, b):
    """Min common even"""
    return (a * b / NSD(a , b))
def main():
    first = int(input("input a "))
    second = int(input("input b "))
    print("NSD %d "%NSD(first,second))
    print("NSK %d "%NSK(first,second))
    
if __name__ == "__main__":
    main()
