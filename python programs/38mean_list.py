a=[]
sum=0
mean=0.0
b=int(input("enter the range for list1:"))
for i in range(b):
    z=int(input("Enter the nos:"))
    a.append(z)
print("original list:",a)
for i in a:
    sum=sum+i
    mean=(sum/2)
print("mean for the list is:",mean)
