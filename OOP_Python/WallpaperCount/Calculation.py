# Класс создает объект с атрибутом площадь объекта
import math
class WinDoor:
    """Class for determining the area of ​​a window or door"""
    def __init__(self,x,y):
        """Constructor, takes the height and width of the object"""
        self.square=x*y
#!!!!Посмотрть по возможности замены расчета площади через метод для окон и дверей
# Созадние класса комнта

class Room:
    """Class Room determining area with room"""
    def __init__(self,x,y,z):
        """Constructor take height, Width and length"""
        #self.square=2*z*(x+y)
        self.height = z
        self.width = y
        self.length = x
        self.wd=[]
    # Метод для расчета площади
    def setSquare (self):
        """Determinimg area room"""
        self.square=2*self.height*(self.width+self.length)
        return self.square
    # Метод для добавления нового окна или двери
    def addWD(self,w,h):
        """Add new window or door. Take two arguments width and height"""
        self.wd.append(WinDoor(w,h))
    # Метод для расчет рабочей поверхности
    def workSurface(self):
        """Determining work place"""
        new_square=self.setSquare()
        for i in self.wd:
            new_square-=i.square
        return new_square
    def kolWalpapper (self,width,length):
        """Determining amount wallpaper. Take two arguments width and length """
        self.squreWallpepper = width*length
        self.rezult = self.workSurface() / self.squreWallpepper
        return math.ceil(self.rezult)
