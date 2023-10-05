a=[]
even=-1
odd=100
b=int(input("enter the range for list1:"))
for i in range (b):
    z=int(input("Enter the nos:"))
    a.append(z)
print("original list:",a)
for i in a:
    num=int(i)
    if (num%2==0 and num>even):
        even=num
    elif (num%2==1 and num<odd):
        odd=num
print("largest even number:",even)
print("smallest odd number:",odd)
