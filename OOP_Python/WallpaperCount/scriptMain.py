import WallpaperCount.Calculation
# основной код
# Проверяем на корректность ввода значения
"""Enter start value"""
widthRoom = input("Enter width room: ")
heightRoom = input("Enter Height room: ")
lengthRoom = input("Enter length room: ")
"""Test for type value float"""
while type(widthRoom) and type(heightRoom) and type(lengthRoom) != float:
    try:
            widthRoom=float(widthRoom)
            heightRoom=float(heightRoom)
            lengthRoom=float(lengthRoom)
            squreRoom =  WallpaperCount.Calculation.Room(lengthRoom, heightRoom, widthRoom)
            """Enter repeat value"""
    except ValueError:

            if type(widthRoom)!=float:
                print("Value width is not correct. Try again")
                widthRoom = input("Enter width room: ")
            elif type(heightRoom)!=float:
                print("Value Height is not correct. Try again")
                heightRoom = input("Enter Height room: ")
            elif type(lengthRoom)!=float:
                print("Value length is not correct. Try again")
                lengthRoom = input("Enter length room: ")



print("Enter amount window and door")

amountWinDoor=input("Amount: ")
"""Test for type value int"""
while not amountWinDoor.isdigit():
    print("Value is not correct. Try again")
    amountWinDoor = input("Amount: ")
else:

    amountWinDoor=int(amountWinDoor)
i=0
while i < amountWinDoor:
    print('Enter size window or door')
   #Проверка коррктности ввода размера окна или двери
    widthWinDoor = input("Enter width window or door: ")
    hightWinDoor= input("Enter hieght window or door: ")
    while type(widthWinDoor) and type(hightWinDoor) != float:
        try:
            widthWinDoor = float(widthWinDoor)
            hightWinDoor = float(hightWinDoor)
            squreRoom.addWD(widthWinDoor,hightWinDoor)
        except ValueError:
            if type(widthWinDoor) != float:
                print("Value width is not correct. Try again")
                widthWinDoor = input("Enter width window or door: ")
            elif type(hightWinDoor)!= float:
                print("Value hieght is not correct. Try again")
                hightWinDoor = input("Enter hieght window or door: ")
    i+=1

#print(squreRoom.square)

#squreRoom.addWD(2,3)
#squreRoom.addWD(4,2)
#Проверка на корректность ввода
"""Test for type value float"""
widthWalpepper = input("Enter width walpepper: ")
hightWalpepper = input("Enter hight walpapper: ")
while type(widthWalpepper) and type(hightWalpepper)!=float:
    try:
        widthWalpepper=float(widthWalpepper)
        hightWalpepper=float(hightWalpepper)
    except ValueError:
        if type(widthWalpepper)!=float:
            print("Value width is not correct. Try again")
            widthWalpepper = input("Enter width walpepper: ")
        elif type(hightWalpepper)!=float:
            print("Value hight is  not correct. Try again")
            hightWalpepper = input("Enter hight walpapper: ")
print("Square room: {0}".format(squreRoom.setSquare()))
print("Work surface: {}".format(squreRoom.workSurface()))
print("Amount walpappers: {}".format(squreRoom.kolWalpapper(widthWalpepper,hightWalpepper)))
print("Square once roll: {}".format(squreRoom.squreWallpepper))
"""Print information"""
#print(help(WallpaperCount.Calculation))