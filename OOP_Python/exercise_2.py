import random
class Warior:
    wariorHelth=100

wariorOne=Warior()
wariorTwo=Warior()

wariorTwo.wariorHelth=100
print(type(wariorTwo.wariorHelth),wariorOne.wariorHelth)

while not wariorOne.wariorHelth <=0 and not wariorTwo.wariorHelth <=0:
    atack=random.randint(1,2)
    if atack==1:
        print('Warior one atack warrior two')
        wariorTwo.wariorHelth-=20
        print("Warrior two helth : {0} ".format(wariorTwo.wariorHelth))

    elif atack==2:
        print("Warrior two atack warrior one")
        wariorOne.wariorHelth-=20
        print("Warior one helth : {0}".format(wariorOne.wariorHelth))
if wariorOne.wariorHelth<wariorTwo.wariorHelth:
    print("Win warrior two")
else:
    print("Win Warrior one")



