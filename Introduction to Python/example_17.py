# примеры из глвавы 17
# crate list
list=[12,3.85,'black',-4]
print(list)
# извлечение первого  и третьего элемента
print(list[0])
print(list[2])
print(list[-1])

# срез элементов
print(list[1:3])
print(list[:])
print(list[:-1])

# изменение элемента на месте
list[1] = 'new'
print(list)

# добавленеи в конец списка
list.append("append")
print(list)

# вставка в список значение в определенный индекс
list.insert(2,"insert")
list.insert(2,4)
list.insert(0,4)
print(list)

# Удаляет первое найденное совпадение
list.remove(4)
print(list)

# удаляет последний элемент или указанный по индексу, есть возможность использовать удаляемое значение
rezDel=list.pop(2)
print(rezDel)
rezDel=list.pop()
print(rezDel)
print(list)

# объединени списко с помощью срезов
listOne = [1,2,3,4,5,6,8]
newList = list[:] + listOne[3:-2]
print(newList)


# измененеи среза значений
newList[1:3]=[123,3456,476]
print(newList)

# заполнение пустого списка случайными числами
import  random
listRandom=[]
number=int(input("Введите количество цифр необходимых для генерации"))
i=0
while i<number:
    listRandom.append(random.randint(0,10000))
    i+=1
print(listRandom)
print(sorted(listRandom))
