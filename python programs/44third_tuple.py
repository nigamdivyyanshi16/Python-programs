a=[]
v=[]
b=int(input("how many elements u want in tuple1: "))
for i in range(b):
    z=int(input("enter the numbers: "))
    a.append(z)
    
b=int(input("\nhow many elements u want in tuple 2: "))
for i in range(b):
    z=int(input("enter the numbers: "))
    v.append(z)
tup3=tuple(a)+tuple(v)
print(tup3)
