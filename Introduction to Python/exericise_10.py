#практическое задание, глава 10 ыункции. Создание вложенных функций

def test():
    number=input("Enter intger number: ")
    while type(number)!=int:
        try:
            number=int(number)
        except ValueError:
            number=input("You enter not integer number.\nTry again:")
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        print("Enter zero")
def positive():
    print("Положительное")

def negative ():
    print("Отрицательное")


test()