from math import sqrt
hall_area = float(input("Input square area: "))
hall_side = sqrt(hall_area)
scene_radius = float(input("Input scene radius: "))
aisle_width = float(input("Input aisle width: "))
if hall_side / 2 > scene_radius:
    if hall_side / 2 - scene_radius > aisle_width:
        print("This scene will fit in this hall!")
    elif hall_side / 2 - scene_radius <= aisle_width:
        print("This scene will not fit in this hall!")
else:    
    print("This scene will not fit in this hall!")
