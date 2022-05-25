#1
str=input("Enter text: ")
print(str)
for i in str:
    if i.isupper():
        print(i.lower(), end='')

    elif i.islower():
        print(i.upper(), end='')
    else:
        print(i,end='')
print()


#2
nuberOne=input("Enter number One: ")
numberTwo=input("Enter number Two: ")
while not numberTwo.isdigit() or not nuberOne.isdigit(): #isdigit проверяет состоит ли строка только из чисел
    if not nuberOne.isdigit():
        nuberOne = input("Enter number One: ")
    elif not numberTwo.isdigit():
        numberTwo = input("Enter number Two: ")

def sum(arg1,arg2):
    arg1=int(arg1)
    arg2=int(arg2)
    sumNumbers=arg1+arg2
    print(sumNumbers)

sum(nuberOne,numberTwo)