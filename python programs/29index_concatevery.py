a=[ ]
m=[ ]
n=[ ]
b=int(input("enter the range for list1:"))
for i in range (b):
    z=int(input("Enter the nos:"))
    a.append(z)
    
c=int(input("enter the range for list2:"))
for i in range (c):
    z=int(input("Enter the nos:"))
    m.append(z)

for j in range(b):
    for k in range(c):
        if j<=k or k<=j:
            n.append(a[j])
            n.append(m[k])
print(n,end="  ")
