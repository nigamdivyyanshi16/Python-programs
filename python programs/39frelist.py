a=[]
ue=[]
de=[]
frequency = {}
b=int(input("enter the range for list1:"))
for i in range(b):
    z=int(input("Enter the nos:"))
    a.append(z)
for item in a:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
        if (frequency[item]>1):
            de.append(item)
        else:
            ue.append(item)
print(frequency)
print("unique element list is",ue)
print("Duplicate element list is",de)
