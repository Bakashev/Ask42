#1
import random
# случайное целое число от 6 до 12
print(random.randint(6,12))
#Число кратное 5 в пределах от 5 до 100
print(random.randrange(5,100,5))

def randonInt(a,b):
    return random.randint(a,b)

def randomFloat(a,b):
    return random.random()*(a-b)+b


try:
    numberDown=int(input("Enter numberDawn"))
    numberUp=int(input("Enter numberUP"))

except ValueError:
    print("Try again")

try:
    choose=int(input("You want recive random number integer or float\nPress 1 if you want recive integer number\nPress "
             "2 if you want recive float number"))
    while choose!=1 and choose!=2:
        choose = int(input("You want recive random number integer or float\nPress 1 if you want recive integer number\nPress "
                  "2 if you want recive float number: "))
    if choose ==1:
        print(randonInt(numberDown,numberUp))
    elif choose==2:
        print(randomFloat(numberDown,numberUp))
except ValueError:
    choose = int(input("You want recive random number integer or float\nPress 1 if you want recive integer number\nPress "
              "2 if you want recive float number: "))


