#Practic 17.2 Generate 100 float number
import random
listFloat=[]
i=0
while i<100:
    listFloat.append(random.random()*(100-0)+0)
    i+=1
print(listFloat)


def printListRow(arg):
    i=0
    while i<10:
        tmp=arg[i:-1:10]
        print(tmp)
        i+=1

def printListStr(arg):
    i=0
    while i<10:
        tmp=arg[i*10:(i*10+10):1]
        print(tmp)
        i+=1


printListRow(listFloat)
listFloat.sort()
print()
print(listFloat)
print()
printListStr(listFloat)
