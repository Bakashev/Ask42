# вывод числа 1 в случае если число положительно, -1 - если отрициательноб 0- если 0 использовать elif
try:
    number=int(input("Введитие число: "))
    if number<0:
        print(-1)
    elif number>0:
        print(1)
    else:
        print(0)

except ValueError:
    print("Введено не число")