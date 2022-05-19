#Практическое задание для главы 7 циклы
#1
total=100

while total>0:
    number = input("Enter number ")
    while type(number)!=int:
        try:
            number = int(number)
        except ValueError:
            number = input("Enter number ")
    if total - number>0:
        total-=number
    else:
        print(str(total- number) + " Значение выходит за границы")
        break
print(total)

#2 вывод степени от 0 до 20 числа 2
i=0
number=2
while i<20:
    print(number**i)
    i+=1