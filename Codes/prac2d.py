############# EXPERIMENT 2.D ###################
# Area of a given shape(rectangle, triangle, and circle) reading shape and 
# appropriate values from standard input.

import math
import argparse
import sys

def rectangle(x,y):
    """
    calculate area and perimeter
    input: length, width
    output: dict - area, perimeter
    """
    perimeter = 2*(x+y)
    area = x*y
    return {"area": area, "perimeter": perimeter}

def triangle(a, b, c):
    p = a + b + c
    s = p/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return {"area": area, "perimeter": p}

def circle(r):
    perimeter = 2*math.pi*r
    area = math.pi*r*r
    return {"area": area, "perimeter": perimeter}

if __name__ == "__main__":
    choices = ["tri", "circ", "rect"]
    parser = argparse.ArgumentParser(
            description="Calculate Area of Basic geometry")
    parser.add_argument("geom", choices=choices, help="Geometry type")
    parser.add_argument('para', type=float, nargs='*',
            help="parameters for geometry")
    args = parser.parse_args()
    if args.geom=="tri":
        ret = triangle(args.para[0], args.para[1], args.para[2])
        print(f"Perimeter: {ret['perimeter']}")
        print(f"Area: {ret['area']}")
    elif args.geom=="rect":
        ret = rectangle(args.para[0], args.para[1])
        print(f"Perimeter: {ret['perimeter']}")
        print(f"Area: {ret['area']}")
    else:
        ret = circle(args.para[0])
        print(f"Perimeter: {ret['perimeter']}")
        print(f"Area: {ret['area']}")




