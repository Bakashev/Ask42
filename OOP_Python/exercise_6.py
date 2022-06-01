class Table:
    __typeTable=''
    __h=0
    __l=0

    def __init__(self,hieght,long,typeT):
        self.__setTable(hieght,long,typeT)
        #self.typeTable = str(typeT)
        #self.l = long
        #self.h = hieght

    def __setTable(self,hieght,long,typeT):
        Table.__h = hieght
        Table.__l = long
        Table.__typeTable=typeT
        
        #self.typeTable = str(typeT)
        #self.l=long
        #self.h=hieght

    def setHieght(self,h):
        Table.__h=h
        #self.h=h
    def setType (self,t):
        Table.__typeTable=str(t)
        #self.typeTable=str(t)

    def setLong (self,l):
        Table.__l=l
        #self.l=l
    def getTable(self):
        return Table.__typeTable, Table.__h, Table.__l
        #return  self.l,self.h,self.typeTable

    def __setattr__(self, key, value):
        print(self.__dict__.keys())
        if key == '__l':
            self.__dict__[key]=value
        elif key == '__h':
            self.__dict__[key] = value
        elif key == '__typeTable':
            self.__dict__[key] = value
        else:
            print(self.__dict__.keys())
            raise AttributeError


t=Table(23,4,"kitchen")
print(t.getTable())
t.setHieght(10000)
print(t.getTable())
t.setLong(22333)
t.setType('desk')
print(t.getTable())
#t.h=9
#print(t)
print(t.getTable())
#t.field1='test'
t.