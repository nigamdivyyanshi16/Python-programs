print('\n' , "1-binary to decimal" , '\n' , "2=decimal to binary")
ch=int(input("enter a choice"))
if (ch==1):
       bin=int(input("enter a binary number"))
       while bin>0:
           d=bin%10
           dec=dec+d*(2**temp)
           bin=bin/10
           temp+=1
       print("decimal of {x} is : {y}".format(x=b,y=d))
if (ch==2):
    dec=int(input("enter a decimal number"))
    temp=0
    while dec>0:
        rem=dec%2
        dec=dec/2
        bin=bin+rem*temp
        temp=temp*10
    print("binary is" ,bin)
        
