n1=int(input("Enter the 1st no"))
n2=int(input("Enter the 2nd no"))
print('\n',"1. add",'\n',"2. subtract",'\n',"3. product",'\n',"4. quotient",'\n',"5. remainder",'\n')
ch=int(input("Enter your choice:"))
if (ch==1):
    s=n1+n2
    print("sum is",s)
if (ch==2):
    d=n1-n2
    print("difference is",d)
if (ch==3):
    p=n1*n2
    print("product is",p)
if (ch==4):
    q=n1/n2
    print("quotient is",q)
if (ch==5):
    r=n1%n2
    print("remainder is",r)
