#Выполнение практического задания глава 12 return
#1 Контенцинация двух строк
def enterSting ():
    firsrStr= input("Enter first sting ")
    secondStr= input("Enter secon string ")
    rezult=  firsrStr.title().lstrip()+" "+secondStr.title()
    return rezult
print(enterSting())

# ПРоизведение введеных с клавиатуры чисел, умножается до тех пор пока не введется 0
def multiply ():
    number=int(input("Enter number: "))
    rezult = 1
    while number!=0:
        rezult*=number
        number = int(input("Enter number: "))
    return rezult

def multiplyTry ():
    number = int(input("Enter number: "))
    rezult = 1
    while number!=0:

        #number=input("Enter number: ")
        try:
            number=int(number)
            rezult*=number
            number=int(input("Enter number: "))
        except ValueError:
            print("Try again!")
            number=int(input("Enter number: "))
    return rezult
print(multiply())
print(multiplyTry())