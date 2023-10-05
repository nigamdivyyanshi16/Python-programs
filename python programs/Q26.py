print("1)Magic number\n2)Is a perfect number\n3)Twisted prime")
ch=int(input("Enter your choice:"))
if (ch==1):
    n=int(input("Enter a number to be checked"))
    s = 0
    while (n > 0 or s > 9):
      if (n == 0):
         n = s
         s = 0
      s = s + n % 10
      n = int(n / 10)
    if s==1:
        print("The given number is Magic Number.")
    else:
        print("The given number is not a Magic Number.")

elif (ch==2):
    num = int(input("Enter any Number: "))
    s = 0
    for i in range(1, (num-1)):
        if(num % i == 0):
            s=s + i
    if (s== num):
        print(" %d is a Perfect Number" %num)
    else:
        print(" %d is not a Perfect Number" %num)

elif(ch==3):
    n=int(input("Enter any Number: "))
    x=n
    flag=False
    rev=0
    while(x>0):
        r=x%10
        rev=rev*10+r
        x=x//10
    print("Reverse is",rev)
    for i in range(2,(n//2+1)):
        if n%i==0:
            flag=True
    for j in range (2,(rev//2+1)):
        if rev%j==0:
            flag=True
    if(flag==True):
        print("Number is not twisted prime")
    else:
        print("Number is twisted prime")
       
else:
    print("Wrong selection")
            
            
        
        
