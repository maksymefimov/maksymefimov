
def distance(x1,y1,x2,y2):
    from math import sqrt 
    d = sqrt((x1-x2)**2+(y1-y2)**2)
    return d
def main():
    print("input cordinates of a point")
    xa = float(input())
    ya = float(input())
    print("input cordinates of a point")
    xb = float(input())
    yb = float(input())
    d_A_B = distance(xa,ya,xb,yb)
    print("The distance = %5.2f"%d_A_B)
