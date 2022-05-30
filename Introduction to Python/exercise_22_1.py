#Practic 22
#Task_one
numbers=['один','два','три','четыре','пять']
i=0
for fileReadline in open("d:\Work\\ask42\Introduction to Python\\data.txt"):
    line = fileReadline
    findValue=fileReadline[:fileReadline.find('-')]
    newLine=numbers[i] + fileReadline[fileReadline.find('-'):]
    i+=1
    fileWriteLine = open("d:\Work\\ask42\Introduction to Python\\dataRU.txt",'a')
    fileWriteLine.write(newLine)
    print(findValue)
    print(line)
    print(newLine)
fileWriteLine.close()

