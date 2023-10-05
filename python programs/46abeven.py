otuple=()
ituple=()
c=0
a=int(input("enter the number of tuple you want to insert"))
for i in range(1,a+1):
    print("\nTuple ",i)
    val1=int(input("enter the 1st value:"))
    val2=int(input("enter the 2nd value:"))
    ituple=(val1,val2)
    otuple=otuple+(ituple,)
    if (val1%2==0) and (val2%2==0):
        c=c+1

print("tuple: ",otuple)
print("No of tuple having both element as even: ",c)
