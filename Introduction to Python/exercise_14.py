# Practic 14
def showValue (arg):
    return chr(arg)


number = input("Enter Unicode: ")
while type(number)!=int:
    try:
        number=int(number)
        while number!=0:
            print(showValue(number))
            number = int(input("Enter Unicode: "))
    except ValueError:
        print("Fail format, try again. ")
        number = input("Enter Unicode: ")


# 2
def lenStr (arg):
    if len(arg)==10:
        print(arg)
    elif len(arg)>10:
        print("Srting len more 10 ")
    else:
        length=10-len(arg)
        print(arg + (length*'*'))

str=input("Enter text: ")
lenStr(str)


#3

"""try:
    
    numberOne=float(input("Enter number one"))
    numberTwo=float(input("Enter number two"))
    numberThree=float(input("Enter number three"))
    numberFour=float(input("Enter number four"))
    numberFive=float(input("Enter number five"))
    numberSix=float(input("Enter number six"))


def minNumber(arg1,arg2,arg3,arg4,arg5,arg6):
    tmp = arg1
    if tmp>arg2:
        tmp=arg2
    elif tmp>arg3:
        tmp=arg3
    elif tmp>arg4:
        tmp=arg4
    elif tmp>arg5:
        tmp=arg5
    elif tmp>arg6:
        tmp=arg6
    return tmp


print(round(minNumber(numberOne,numberTwo,numberThree,numberFour,numberFive,numberSix),2))"""

numbers=[]
while len(numbers)<6:
    try:
        number=float(input("Enter float number"))
        numbers.append(number)
    except:
        print("Try again")
print(numbers)

def minNumbers (arg):
    tmp=arg[0]
    for i in arg:
        if tmp>i:
            tmp=i
    return tmp

def maxNumbers (arg):
    tmp=arg[0]
    for i in arg:
        if tmp<i:
            tmp=i
    return tmp
print(round(minNumbers(numbers),2))
print(round(maxNumbers(numbers),2))