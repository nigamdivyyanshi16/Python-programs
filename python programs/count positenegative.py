r=int(input("enter a range:"))
p=0
cp=0
n=0
cn=0
zn=0
for i in range(r):
    num=int(input("enter a number:"))
    if(num>1):
        p=p+num
        print("positive :" ,p)
        cp=cp+1
        print("positive count:" ,cp)
        break
    elif(num<1):
        n=n+num
        print("negative :" ,n)
        cn=cn+1
        print("negative count:" ,cn)
        break
    elif(num==0):
        zn=zn+1
        print("zero count:",zn)
        break
    elif(num==-1):
        print("terminate")
        break
