print(" 1) Prime number",'\n',"2) Armstrong number")
ch=int(input("Enter your choice:"))
flag=False
s=0
if (ch==1):
    lower = int(input("Enter the lower value:"))
    upper = int(input("Enter the upper value:"))
    print("Prime number in range ")
    for number in range(lower,upper+1):
        if number>1:
            for i in range(2,number):
                if (number%i)==0:
                    break
            else:
                print(number)
elif (ch==2):
    l= int(input("Enter lower range: "))
    u = int(input("Enter upper range: "))
    print("Armstrong number in range ")
    for n in range(l, u + 1):
        p = len(str(n))
        s = 0
        t= n
        while t > 0:
            digit = t % 10
            s+= digit **p
            t //= 10

        if n == s:
                print(n)

else:
    print("Wrong choice")
    
