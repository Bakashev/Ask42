from math import pi
class Cilinder:
    @staticmethod
    def _make_area(d,h):
        circle=pi*d**2/4
        side=pi*d*h
        return round(circle*2+side,2)
    def __init__(self,diametr,high):
        #self._d=diametr
        #self._h=high
        self._d=diametr
        self._h=high
        self._area= self._make_area(self._d,self._h)
    def setDiametr(self,diametr):
        self._d=diametr
        self._area=self._make_area(self._d,self._h)
    def setHigh(self,high):
        self._h=high
        self._area = self._make_area(self._d,self._h)
    def getArea(self):
        return self._area

    def __setattr__(self, key, value):
        if key =='_d':
            self.__dict__[key]=value
         #   self._area=self._make_area(self.d,self.h)
        elif key == '_h':
            self.__dict__[key] = value
        elif key == '_area':
            self.__dict__[key] = value

        else:
                raise AttributeError
        #self._area = self._make_area(self.d, self.h)
a=Cilinder(1,2)
#print(a.area)
#print(a.make_area(2,2))
#print(a.getArea())
#a.setDiametr(3)
print(a.getArea())
#a.setHigh(4)
print(a.getArea())
a.setDiametr(5)
print(a.getArea())
a.setHigh(4)
print(a.getArea())

