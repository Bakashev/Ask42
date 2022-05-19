import areaFigure
choose = input("Chose:\n 1. Area rectangle \n 2. Area triangle \n 3. Area circle\n your choose: ")
while type(choose)!=int:
    try:
        choose=int(choose)
    except:
        choose = input("Try arain \nChose:\n 1. Area rectangle \n 2. Area triangle \n 3. Area circle")

if choose==1:
    areaFigure.rectangle()
elif choose==2:
    areaFigure.triangle()
elif choose==3:
    areaFigure.circle()
else:
    print("You choose is fail, try again")
