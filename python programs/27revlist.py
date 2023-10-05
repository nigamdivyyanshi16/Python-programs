a=[]
m=[]
b=int(input("enter the range:"))
for i in range (b):
    z=int(input("Enter the nos:"))
    a.append(z)
print(a)
print("reversed list is:")
for j in range(b-1,-1,-1):
    m.append((a[j]))
print(m)
