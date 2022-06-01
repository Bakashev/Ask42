class B:
    __count=0
    def __init__(self):
         B.__count+=1
    def __del__(self):
         B.__count-=1
    def qtyCount():
        return B.__count
a=B()
b=B()
print(B.qtyCount())
b.__del__()
print(B.qtyCount())
#B.count=3
#print(B.queCount())

class DubleList:
    def __init__(self,l):
        self.doubleList=DubleList.__copyList(l)
    def __copyList (old):
        new=[]
        for i in old:
            new.append(i)
            new.append(i)
        return new
list=DubleList([1,2,3,4,5,6,7])
print(list.doubleList)
#print(list._copyList([1,2]))

class A:
    def __init__(self,v):
        self.field1=v
    def __setattr__(self, key, value):
        if key=='field1':
        #print(self.__dict__.keys())
        #if key in self.__dict__.keys():
            self.__dict__[key]=value
        else:
            print(self.__dict__.keys())
            raise AttributeError
a=A(20)
a.field2=10
print(a.field1)
