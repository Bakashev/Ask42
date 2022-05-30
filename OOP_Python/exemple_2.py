class A:
    pass
a=A()
b=A()

class B:
    n=5
    def adder (self,v):
        return v+self.n

print(B.n)
#print(B.adder(12))

l=B()
l.n=10
m=B()
print(l.n)
print(l.adder(5))
print(m.adder(5))
print(l.n is m.n)
print(B.n is m.n)


l.test='Hi'
#B.test='No'
print(l.test)
#print(B.test)

class User:
    def setName(self,n):
        self.name=n

    def getName(self):
        try:
            return self.name
        except:
            print("No name")

first=User()
second=User()
first.setName('Bob')
print(first.getName())
second.getName()

