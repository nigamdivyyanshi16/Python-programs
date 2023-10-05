a=[]
b=int(input("enter the range:"))
for i in range (b):
    z=int(input("Enter the nos:"))
    a.append(z)
print("original list:",a)
nums=[]
zero=[]
for i in range(len(a)):
    if a[i]!=0:
        nums.append(a[i])
    else:
        zero.append(a[i])
print(nums+zero)
