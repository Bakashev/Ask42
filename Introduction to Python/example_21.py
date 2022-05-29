# примеры из главы 20
dictonary={"cat":"кошка", "dog":"собака", "parrot":"попугай", "bird":"птица", "mouse":"мышь"}
print(dictonary)
print(dictonary["mouse"])
dictonary['elefant']='слон'
dictonary['cat']='КОШКА'
del dictonary["bird"]
print(dictonary)

nums={1:'one',2:'two',3:'three'}
person= {'name':'Tom', 1:[30,15,16],2:2.34, ('ab',100):'no'}
print(person[('ab',100)])

for i in nums:
    print(nums[i])
n=nums.items()
print(n)

for keys,values in nums.items():
    print(keys, 'is', values)

v_nums=[]
for value in nums.values():
    v_nums.append(value)
print(v_nums)

k_nums=[]
for key in nums.keys():
    k_nums.append(key)
print(k_nums)

#clear() удаляет значения словаря но не сам словарь
dict_clear={1:'one',2:'two'}
print(dict_clear)
dict_clear.clear()
print(dict_clear)
# copy()
numstwo=nums.copy()
print(nums)
print(numstwo)

#fromkeys()
a=[1,2,3]
c=dict.fromkeys(a)
print(c)
d=dict.fromkeys(a,10)
print(d)
print(c)

#get получение элкмента по ключу
print(person.get(2))# равносильно person[2]

#pop() and popitem()
print(person)
person.popitem()
print(person)
person.pop('name')
print(person)

#setdefault
nums.setdefault(7,"seven")
print(nums)
nums.setdefault(7,'sevenS')
print(nums)

#update
nums.update({7:'SEVENES',9:'nine'})
print(nums)
