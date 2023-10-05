d=[]
n=[]
b=0
c=0
a=int(input("enter the range for list1:"))
for i in range (a):
    z=int(input("Enter the nos:"))
    n.append(z)
    if n[i]%2!=0:
        b=n[i]*n[i]
        d.append(b)
    elif n[i]%2==0:
        c=n[i]*n[i]*n[i]
        d.append(c)  
    
print(d,end='')
