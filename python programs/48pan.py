u=input("Enter a username:")
p=input("Enter the PAN number:")
z=len(p)
if (z!=10):
    print("Enter a 10 digit valid PAN card number")
    p=input("Enter the PAN number:")
print("USERNAME:",u)
print("PAN NUMBER:",p)
