#введение в исключение
numberA = input("Введите число А: ")
numberB = input("Введитие число В: ")
try:
    if int(numberA) or int(numberB):
       print(int(numberA) + int(numberB))
except ValueError:
    print(numberA + numberB)
finally:
    print("Конец работы программы")
