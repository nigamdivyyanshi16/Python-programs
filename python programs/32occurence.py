a=[]
m=[]
b=int(input("enter the range:"))
for i in range (b):
    z=int(input("Enter the nos:"))
    a.append(z)
print(a)
rem=int(input("Enter a number to be removed"))
for item in a:
    if(item!=rem):
        m.append(item)

print("Final list")
print(m)
