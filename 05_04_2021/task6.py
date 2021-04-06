from math import pi
from math import sqrt
print("MENU \n1.Square of rectangle\n2.Square of triangle\n3.Square of circle")
choice = int(input("Input ypur choice: "))
if choice == 1:
    print ("RECTANGLE SQUARE")
    rectangle_lenght = float(input("Input rectangle lenght(cm): " ))
    rectangle_width = float(input("Input rectangle width(cm): "))
    print("Rectangle square: ",rectangle_lenght * rectangle_width)
elif choice == 2:
    print ("TRIANGLE")
    triangle_leg1 = float(input("Input triangle Leg1(cm): "))
    triangle_leg2 = float(input("Input triangle Leg2(cm): "))
    triangle_hypo = float(input("Input triangle hypotenuse(cm): "))
    triangle_square = (triangle_leg1+triangle_leg2+triangle_hypo)/2
    triangle_square = sqrt(triangle_square*(triangle_square-triangle_leg1)*\
            (triangle_square-triangle_leg2)*(triangle_square-triangle_hypo))
    print("Triangle square(cm): ",triangle_square)
elif choice == 3:
    print ("CIRCLE")
    circle_radius = float(input("Input circle radius(cm): "))
    print("Circle square: ",pi * (circle_radius ** 2))
else:
    print("Unknown choice!!!")
