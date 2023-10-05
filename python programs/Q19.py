print(" 1) Decimal to binary",'\n',"2) Binary to decimal")
ch=int(input("Enter your choice:"))

if (ch==1):
    d=int(input("Enter a decimal number:"))
    b=0
    ctr=0
    t=d
    while(t>0):
        b=((t%2)*(10**ctr)) + b
        t=int(t/2)
        ctr+= 1    
    print("Binary of {x} is: {y}".format(x=d,y=b))
        
elif (ch==2):
    b=int(input("Enter a Binary Number: "))
    d=0
    m=1
    l=len(str(b))
    for i in range(l):
        r=b%10
        d=d+(r*m)
        m=m*2
        b=int(b/10)

    print("Equivalent Decimal Value = ", d)
    
else:
    print("Wrong choice")
