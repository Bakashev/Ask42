class A:
    a=10
    def __add__(self, other):

        return A()
a=A()
b=A()
print(a)
print(a+12+1)
print(a +'qwe')
print(b + a)