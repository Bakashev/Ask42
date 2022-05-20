# Практическое задание для главы 11 Локальные и глобальные переменные0
import math
high=input("Enter high cilinder: ")
radius = input("Enter high radius: ")
def cylinder():
    choose = input("1. Расчитать площадь боковой поверхности цилиндра \n2.Расчитать площадь цилиндра\nYour choose")
    while type(choose)!=int:
        try:
            choose=int(choose)
        except ValueError:
            choose  = input("1. Расчитать площадь боковой поверхности цилиндра \n2. Расчитать площадь цилиндра\nYour choose")
    if choose==1:
            global high
            global radius
            while type(high) and type(radius) !=float:
                try:
                    high=float(high)
                    radius=float(radius)
                except ValueError:
                    print("Введено недопустимое значение. Попробуйте еще")
                    if type(high)!= float:
                        high = input("Enter high cilinder: ")
                    elif type(radius)!=float:
                        radius = input("Enter high radius: ")
            areaOne=2*math.pi*high*radius
            print("Боковая площадь ровна %.2f"% areaOne)
    elif choose==2:
        #high = input("Enter high cilinder: ")
        #radius = input("Enter high radius: ")
        while type(high) and type(radius) != float:
            try:
                high = float(high)
                radius = float(radius)
            except ValueError:
                print("Введено недопустимое значение. Попробуйте еще")
                if type(high) != float:
                    high = input("Enter high cilinder: ")
                elif type(radius) != float:
                    radius = input("Enter high radius: ")
        areaOne = 2 * math.pi * high * radius + (2*circle())
        print("Площадь ровна %.2f" % areaOne)
    else:
        print("ВЫбран не верный пункт попробуйте еще")

def circle ():
    #radius=input("Enter radius: ")
    global radius
    while type(radius)!=float:
        try:
            radius=float(radius)
        except ValueError:
            radius=input("Enter radius: ")
    areaCircle = math.pi * radius**2
    return areaCircle

cylinder()
#print("Area circle  = %.2f" % circle()[1])