a=int(input("Enter the 1st no"))
b=int(input("Enter the 2nd no"))
c=int(input("Enter the 3rd no"))
print("Maximum is" '\n')
if (b<= a >=c):
    print(a)
elif (a<= b >=c):
    print(b)
elif(a<= c >=b):
    print(c)
print("mimimum is"'\n')
if (a<b):
    if(a<c):
        print(a)
elif (b<a):
    if(b<c):
        print(b)
elif (c<a):
    if(c<a):
        print(c)
