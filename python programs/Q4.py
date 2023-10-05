i=int(input("Enter the price of item:"))
p=int(input("Enter the tax in percentage:"))
d=int(input("Enter the discount in percentage:"))
y=(p/100)*i
z=(d/100)*i
n=(i+y)-z
print("Net amount to be paid is: ",n)
