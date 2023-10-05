print(" 1) Prime number",'\n',"2) Armstrong number")
ch=int(input("Enter your choice:"))
flag=False
s=0
if (ch==1):
    p=int(input("Enter a number:"))
    if (p>1):
        for i in range (2,int(p/2)):
            if (p%i)==0:
                flag=True
                break
    if (flag==True):
        print(p, "is not prime")
    else:
        print(p, "is prime")
        
elif (ch==2):
    a=int(input("Enter a number:"))
    t=a
    while t>0:
        d=t%10
        s=s+d**3
        t=t//10
    if (a==s):
        print(a,"is an armstrong number")
    else:
        print(a,"is not an armstrong number")
    
else:
    print("Wrong choice")
    
