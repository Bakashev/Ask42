# Заполнение списка случайными числами
#
import random
listRandom=[]
for element in range(20):
    listRandom.append(random.randint(-100,100))
print(listRandom)

# Создание списка с помощью range со значениями от 0-100 с шагом 17
listRandomTwo=list(range(0,100,17))
print(listRandomTwo)

#подсчет отрицательных элементов
count=0
for element in listRandom:
    if element<0:
        count+=1
print(count)


#Ввод слов и подсчет их длинны
texts=[]
longElements=[]
for i in range(5):
    texts.append(input("Enter word: "))
    longElements.append(len(texts[i]))
print(texts)
print(longElements)