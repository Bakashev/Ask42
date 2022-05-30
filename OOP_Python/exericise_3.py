class Person:
    def __init__(self, name,serename, quali=1):
        self.name=name
        self.serename=serename
        self.qualti=quali

    def __del__(self):
        print("Досвидания {0} {1}".format(self.name, self.serename))

    def getPerson(self):
       try:

           return str(self.name) + ' ' + str(self.qualti) + ' ' +  str (self.serename)
       except:
           return 'Object not found'



personOne=Person('Sergey','Bakashev')
print(personOne.name, personOne.qualti,personOne.serename)
print(personOne.getPerson())


personTwo=Person('Stephan', 'Ivanovich', 3)
personThree = Person('Petr', 'Petrovich', 2)
personFour= Person('Iliya', 'Juk',1)
print(personOne.getPerson(), personTwo.getPerson(),personFour.getPerson())
del personTwo
#print(personOne.getPerson(), personTwo.getPerson(),personFour.getPerson())
end=input("Press enter to finish")
if end=='':
    print('Finish')
else:
    del personThree
    del personFour
    del personOne

