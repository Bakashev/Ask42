#Практическое задание глава 13 Аргументы функций
# #1 Функция не имеет параметров, запрашивает ввод с клавиатуры и возвращает веденный текст
def getInput():
    str = input("Enter text: ")
    return str
print(getInput())
# 2Function testInput whith one parametr, if argument = nuber return True else False
def testInput(str):
    try:
        str=int(str)
        return True
    except ValueError:
        return False
print(testInput(input("Enter text or number")))

#3 Function whith one parametr, retrun int(parametr)
def strToInt(arg):
    try:
        arg=int(arg)
        return arg
    except ValueError:
        war="Not number"
        return war
print(strToInt(input("Enter text: ")))

#4 Show on display
def printInt(arg):
    print(arg)
printInt(input("Enter text: "))
