class T1:
    n=10
    def total(self,N):
        self.total=int(self.n)+int(N)
        return self.total

class T2:
    def total(self,s):
        self.total=len(str(s))
        return self.total

t1=T1()
print(t1.total(23))
t2=T2()
print(t2.total(23))

class Rectangle:
    def __init__(self,width,height, sign):
        self.w = int(width)
        self.h=int(height)
        self.s=str(sign)
    def __str__(self):
        rect=[]
        for i in range(self.h):
            rect.append(self.s * self.w)
        rect='\n'.join(rect)
        return rect


c=Rectangle(4,6,'[')
print(c)
#print(c)
#print(c)