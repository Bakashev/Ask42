#practic 22
#task 2
fileRead=open('d:\Work\\ask42\Introduction to Python\\nums.txt','r')
str=fileRead.read().split()
print(str)
sum=0
for i in str:
    sum+=int(i)
print(sum)