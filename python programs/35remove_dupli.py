a=[]
c=[]
b=int(input("enter the range for list1:"))
for i in range (b):
    z=input("Enter the elements:")
    a.append(z)
print("original list:",a)
for i in a:
    if i not in c:
        c.append(i)
print("final list:",c)

