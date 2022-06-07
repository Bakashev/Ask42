import  math
class Snow:
    def __init__(self,amountSnow):
        self.amountSnows = amountSnow

    # Перегрузка сложения
    def __add__(self, other):
        self.__otherAdd=other
        self.amountSnows += self.__otherAdd
        return self.amountSnows
    # Перегрузка вычитания
    def __sub__(self, other):
        self.__otherSub=other
        self.amountSnows -= self.__otherSub
        return self.amountSnows

    #Перегрузка умножения
    def __mul__(self, other):
        self.__otherMul=other
        self.amountSnows *= self.__otherMul
        return int(self.amountSnows)

    #Перегрзка деления
    def __truediv__(self, other):
        self.__otherTruediv = other
        self.amountSnows /= self.__otherTruediv
        return math.ceil(self.amountSnows)

    # Вывод на печать
    def makeSnow (self, amountRow):
        self.__amountRow=amountRow
        str=''
        while self.amountSnows - self.__amountRow > 0:
            for i in range(self.__amountRow):
                str=str+'*'
            self.amountSnows -= self.__amountRow
            str = str + '\\n'
            if self.amountSnows<self.__amountRow:
                for i in range(int(self.amountSnows)):
                    str = str + '*'
                str=str+'\\n'
        return str
    # перезапись amounSnows
    def __call__(self, args):
        self.amountSnows=args
        return self.amountSnows
str=input("Enter amount")

while not str.isdigit():
    str = input("Enter amount")
else:
    str = int(str)
    amountSnow = Snow(str)

print(amountSnow.amountSnows)
print(amountSnow.__add__(30))
print(amountSnow.__truediv__(3))
print(amountSnow.__mul__(3))
print(amountSnow.__sub__(2))
print(amountSnow.makeSnow(5))
amountSnow(10)
print(amountSnow.amountSnows)
