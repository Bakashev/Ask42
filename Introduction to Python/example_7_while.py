# примеры из главы циклы while
# ВВод числа и возведение его в степень
number=input("Enter number: ")
while type(number)!= int:
    try:
        number = int(number)
    except ValueError:
        number=input("Enter number: ")

squ=number**2
print(squ)
if number%2==0:
    print("Четное")
else:
    print("Нечетное")

# examle two
total=100
n=0
while n<5:
    try:
        number=int(input("Enter number"))

    except ValueError:
        print("Введено не число")
        number=int(input("Enter number"))
    total = total - number
    n += 1
    print(total)

#Ввод чисел пока Total ,больше 0

total=100
while total>0:
    try:
        number=int(input("Enter number "))
    except ValueError:
        number=int(input("Try again"))
    total-=number
print("Total empty" + str(total))