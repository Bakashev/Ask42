# примеры из главы 22 Файлы

f1=open("d:\Work\\ask42\Introduction to Python\data.txt",'r')
# считывает 10 байт
print(f1.read(10))
# считывает оставшейся текст
print(f1.read())
print(type(f1.read()))
#считывает построчно
f1=f1=open("d:\Work\\ask42\Introduction to Python\data.txt",'r')
print(f1.readline())
print(f1.readline())
print(f1.readline())
# Считывает все строки и создает список строк readlines
f1=open("d:\Work\\ask42\Introduction to Python\data.txt",'r')
print(f1.readlines())

for i in open("d:\Work\\ask42\Introduction to Python\data.txt"):
    print(i)

# создание списка без дополнителных строк
nums=[]
for num in open("d:\Work\\ask42\Introduction to Python\data.txt"):
    nums.append(num[:-1])
print(nums)

#запись данных
l=['three\n','four']
f2=open("d:\Work\\ask42\Introduction to Python\\newdata.txt",'w')
f2.write('one\n')
print(f2.write('one\n'))
f2.write('two\n')
f2.writelines(l)
print(f1.closed, f2.closed)
f1.close()
f2.close()
print(f1.closed,f2.closed)