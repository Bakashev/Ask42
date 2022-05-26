# Practic 20
#1
list=[3,4,5,6]
def changeList (arg1):
    list=arg1.copy()
    for i in range(len(list)):
        list[i]+=3
    return list
print(list)
print(changeList(list))

def changeListTwo(arg1):
    list=arg1[:]
    for i in range(len(list)):
        list[i]+=4
    return list
print(changeListTwo(list))

#2

import random
def randomTuple():
    randomTupleOne=[]
    for i in range(10):
        randomTupleOne.append(random.randint(0,5))
    randomTupleOne=tuple(randomTupleOne)

    rundomTupleTwo=[]
    for i in range(10):
        rundomTupleTwo.append(random.randint(-5,0))
    rundomTupleTwo=tuple(rundomTupleTwo)

    return randomTupleOne, rundomTupleTwo

print(randomTuple())
tupleThree= randomTuple()[0]+randomTuple()[1]
print(tupleThree)
print(tupleThree.count(0))