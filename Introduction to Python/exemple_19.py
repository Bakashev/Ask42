# работа с символами строк
str="My words"
print(str[0])
print(str[:-2])
print(str[::2])

str=str[:]+" New , text"
print(str)

# разделение строки по пробелу Split
str=input("Enter string: ")
print(str.split())
print(str.split('e'))
# формирует из списка строку с указание разделителя

print("-".join(str))

# Поиск подстроки в строке
str="blue green orange white"
print(str.find("green"))
print(str.find("red"))
print(str.find("a",4,-1))

#Замена найденого значение на другое
str="QWERTGFDA"
print(str.replace("DA","NOTITEM"))
str2=str.replace("DA",'22')
print(str,str2)


#format
size="length - {2}, width- {0}, high - {1}"

print(size.format(3,5,4))