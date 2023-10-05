a=int(input("Enter the 1st no"))
b=int(input("Enter the 2nd no"))
c=int(input("Enter the 3rd no"))
if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
print (a, "<", b, "<", c)
