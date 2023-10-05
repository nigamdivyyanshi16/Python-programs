x=int(input("Enter the numerator value:"))
s=0
s1=0
z=0
j=0
f=1
for i in range(1,x+1):
    f=f*i
    if(i%2==0):
        s=s+int((x**i)/f)
    if (i%2!=0):
        s1=s1+int((-x**i)/f)
z=s+s1
print("The sum is",1+z)

