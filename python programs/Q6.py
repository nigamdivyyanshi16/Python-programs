n1=int(input("Enter the 1st no"))
n2=int(input("Enter the 2nd no"))
n3=int(input("Enter the 3rd no"))
if (n1==n2==n3):
    print("duplicate sum is 0")

elif (n1==n2):
    print("value is",n3)
elif (n1==n3):
    print("value is",n2)

elif (n2==n3):
    print("value is",n1)

else:
    print("sum is",n1+n2+n3)
