# Прмеры из главы 17
list=[123,35,56,7,345,2]
for i in list:
    print(i+2)

# изменение эллементов списка
i=0
for element in list:
    list[i]=element+2
    i+=1
print(list)

# генерация последовательности чисел
a=range(4)
b=range(4,10)
c=range(0,10,2)
print(a,b,c,sep=' - ')

print(a[2])
print(a[0])
print(c[-1])

for element in range(len(list)):
    list[element]=list[element]*10
print(list)