#Practic task 1
school={'1a':20,'1б':23,'2б':30, '2в':19,'7а': 22,'9б':28}
#в 9б-уменьшилась учащихся до 25
print(school)
school['9б']=25
print("People whith 9б: ",school['9б'])
# В школе появился новый класс 9с, 9В, 9Г
school.setdefault('9c',23)
school.update({'9В': 24})
school['9Г']=27
school
print(school)

# Удален 2в
school.pop('2в')
print(school)

count=0
for value in school.values():
    count+=value
print(count)

#practic task 2
dictonary_numbers={1:'one',2:'two', 3:'three', 4:'four', 5:'five'}
print(dictonary_numbers)
dic_items=dictonary_numbers.items()
print(dic_items)
def dict_rev(arg):
    dict_rev={}
    for val in arg:
        dict_rev[val[1]]=val[0]
    return dict_rev
print(dict_rev(dic_items))