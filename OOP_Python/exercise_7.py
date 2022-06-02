# Класс создает объект с атрибутом площадь объекта
import math
class WinDoor:
    def __init__(self,x,y):
        self.square=x*y
#!!!!Посмотрть по возможности замены расчета площади через метод для окон и дверей
# Созадние класса комнта

class Room:
    def __init__(self,x,y,z):
        #self.square=2*z*(x+y)
        self.height = z
        self.width = y
        self.length = x
        self.wd=[]
    # Метод для расчета площади
    def setSquare (self):
        self.square=2*self.height*(self.width+self.length)
        return self.square
    # Метод для добавления нового окна или двери
    def addWD(self,w,h):
        self.wd.append(WinDoor(w,h))
    # Метод для расчет рабочей поверхности
    def workSurface(self):
        new_square=self.setSquare()
        for i in self.wd:
            new_square-=i.square
        return new_square
    def kolWalpapper (self,width,length):
        self.squreWallpepper = width*length
        self.rezult = self.workSurface() / self.squreWallpepper
        return math.ceil(self.rezult)

# основной код
widthRoom = float(input("Enter width room: "))
heightRoom = float(input("Enter Height room: "))
lengthRoom = float(input("Enter length room: "))
squreRoom=Room(lengthRoom,heightRoom,widthRoom)
print("Enter amount window and door")
amountWinDoor=int(input("Amount: "))
i=0
while i < amountWinDoor:
    print('Enter size window or door')
    widthWinDoor = float(input("Enter width window or door: "))
    hightWinDoor= float(input("Enter hieght window or door: "))
    squreRoom.addWD(widthWinDoor,hightWinDoor)
    i+=1

#print(squreRoom.square)

#squreRoom.addWD(2,3)
#squreRoom.addWD(4,2)
print("Square room: {0}".format(squreRoom.setSquare()))
print("Work surface: {}".format(squreRoom.workSurface()))
print("Amount walpappers: {}".format(squreRoom.kolWalpapper(2,3)))
print("Square once roll: {}".format(squreRoom.squreWallpepper))



