# Перегрузка
class A:
    def __init__(self, arg):
        self.arg=arg
    def __str__(self):
        return str(self.arg)


class B:
    def __init__(self, *args):
        self.aList = []
        for i in args:
            self.aList.append(A(i))

    def __getitem__(self, item):
        return self.aList[item]

group = B(12,23,'sdf')
print(group.aList[1])
print(group.aList[2])
print(group[0])

# метлд __call__
class Changeable:
    def __init__(self,color):
        self.color=color
    def __call__(self, newColor):
        self.color = newColor

    def __str__(self):
        return '%s'%self.color
canvas=Changeable('red')
frame=Changeable('yellow')
print(canvas.color)
print(frame.color)
frame('green')
print(frame,canvas)


#метод __str__
class A:
    def __str__(self):
        return "This is obbject of A"
a=A()
print(a)
print(str(a))
print(repr(a))

#__repr__
a='3+2'
b=repr(a)
print(a)
print(b)
print(eval(a))
print(eval(b))
c='Hellow\nWorld'
d=repr(c)
print(c)
print(d)
