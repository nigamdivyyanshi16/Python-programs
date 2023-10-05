a= int(input("Enter the range:"))
p=0
n=0
cp=0
cn=0
c=0
for i in range (a):
        z=int(input("Enter a number for exit enter -1"))
        if (z>=1):
            p=p+z
            cp=cp+1
        elif (z<-1):
            n=n+z
            cn=cn+1
        elif (z==0):
            c=c+1
        elif (z==-1):
            print("terminate")
            break
print("total positive numbers =", cp)
print("total negative numbers =", cn)
print("total number of zeroes=", c)
print("Average of positive numbers=",(p/cp))
print("Average of negative numbers=",(n/cn))

