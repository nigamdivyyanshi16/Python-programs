a=[]
c=[]
b=int(input("enter the range for list1:"))
for i in range (b):
    z=input("Enter the elements:")
    a.append(z)
print("original list:",a)
for i in range(len(a)-1,len(a)):
    c.append(a[i])
for i in range (0,len(a)-1):
    c.append(a[i])
print("final list:",c)

