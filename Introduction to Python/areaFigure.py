def rectangle ():
    a=input("Enter a:")
    b=input("Enter b: ")
    while type(a) and type(b) != float:
        try:
            a=float(a)
            b=float(b)

           #print(type(a),type(b))

        except ValueError:
            if type(a) != float:
                a = input("Enter a: ")
            elif type(b) != float:
                b = input("Enter b:")
            print(type(a), type(b))
    print("Area rectungle = %.2f" % (a*b))

def triangle ():
    a= input("Enter a: ")
    h = input(" Enter h: ")
    while type(a) and type(h)!=float:
        try:
            a=float(a)
            h=float(h)
        except ValueError:
            if type(a)!=float:
                a=input("Enter a: ")
            elif type(h)!=float:
                h=input("Enter h: ")
    print("Area triangle = %.2f" % (0.5 * a * h))
import math
def circle ():
    r = input("Enter r: ")
    while type(r) != float:
        try:
            r=float(r)
        except ValueError:
            r=input("Enter r: ")
    print(" Area circle = %.2f" % (math.pi * r**2))