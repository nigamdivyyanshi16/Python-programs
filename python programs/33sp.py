a=[]
s=0
p=1
b=int(input("enter the range:"))
for i in range (b):
    z=int(input("Enter the nos:"))
    a.append(z)
    s=s+a[i]
    p=p*a[i]
print("The list is \n",a)
print("sum of elements is", s)
print("product of elements is", p)
