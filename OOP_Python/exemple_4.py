class Table:
    def __init__(self, l, w, h):
        self.lenght=l
        self.widdth=w
        self.height=h
class KitchenTable (Table):
    def setPlaces(self,p):
        self.places=p

class DeskTable(Table):
    def square(self):
        return self.widdth*self.lenght
class ComputerTable(DeskTable):
    def square(self,e):
        return self.widdth*self.lenght-e
    #Дополнение return DeskTable.square(self)-e

t1=KitchenTable(2,2,0.7)
t2=DeskTable(3,4,5)
t3=KitchenTable(1,1.2,0.8)
print(t2.square())
t4=ComputerTable(2,3,4)

print(t4.square(4))