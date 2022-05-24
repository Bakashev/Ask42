# Practic

#1
listAdd=[]
i=1
while i<9:
    try:
        number = int(input("Enter number " + str(i) + ": "))
        listAdd.append(number)
        i+=1
    except ValueError:
        number = input("Enter number " + str(i) + ": ")
print("Summa = %.f" % sum(listAdd))
print("Min number = %.2f" %min(listAdd))
print("Max number = %.2s"%max(listAdd))