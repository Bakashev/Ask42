#Practic
import random
class Character:
    uniqueCode = 1000
    def __init__(self,t):
        self.uniqueCode = Character.uniqueCode+1
        Character.uniqueCode+=1
        self.team = t


class Warrior(Character):
    def followTheHero (self, n):
        #self.name=n
        #print(n.uniqueCode, self.uniqueCode)
        return n.uniqueCode, self.uniqueCode

class Hero (Character):
    def __init__(self,t,l=0):
        Character.__init__(self,t)
        self.level=l

    def skilUp(self):
        self.level+=100
        return self.level


herowOne=Hero('blue')
herowTwo=Hero('red')
print(herowOne.uniqueCode,herowOne.team,herowTwo.team,herowTwo.uniqueCode)
teamBlue=[]
teamRed=[]
for i in range(10):
    name='Sold'+str(i)
    team=['blue','red']
    name=Warrior('{}'.format(random.choice(team)))

    if name.team == team[0]:
        teamBlue.append(name)
    elif name.team == team[1]:
        teamRed.append(name)
    print(name.uniqueCode,name.team)
#print(temRed,teamBlue)
print(' red team {0} kol {1} \n blue team {2} kol {3} '.format(teamRed, len(teamRed), teamBlue, len(teamBlue)))
if len(teamBlue)>len(teamRed):
    herowOne.skilUp()
elif len(teamBlue)<len(teamRed):
    herowTwo.skilUp()
print(' level heroe blue {0}\n level heroe red {1} '.format(herowOne.level, herowTwo.level))

print("Warrior {1} follow the Heroe {0}".format(teamBlue[0].followTheHero(herowTwo)[0]
                                               ,teamBlue[0].followTheHero(herowTwo)[1]))

#print(name.name)