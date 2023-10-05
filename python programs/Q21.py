print("1)sum of digits \n2)sum of even digit and product of odd \n3) reverse of number \n4) Pallindrome")
ch=int(input("Enter the choice:"))
if (ch==1):
    n=int(input("Enter a number:"))
    tot=0
    while(n>0):
       dig=n%10 
       tot=tot+dig 
       n=n//10       
    print("The total sum of digits is:",tot)
    
elif (ch==2):
    n=int(input("Enter a number:"))
    s=0
    prod=1
    while(n>0):
        dig=n%10 
        n=n//10
        if (dig%2==0):
            s=s+dig
        elif (dig%2!=0):
            prod=prod*dig
              
    print("The sum of even digits is",s)
    print("The product of odd digits is",prod)

elif (ch==3):
    n=int(input("Enter a number:"))
    r=0
    while(n>0):
       dig=n%10 
       r=r*10+dig
       n=n//10       
    print("The reverse is:",r)

elif (ch==4):
    n=int(input("Enter a number:"))
    t=n
    r=0
    while(n>0):
       dig=n%10 
       r=r*10+dig
       n=n//10       
    if (r==t):
        print(t,"is pallindrome")
    else:
        print(t,"is not pallindrome")

