x=int(input("Enter the numerator:  "))
n=int(input("Enter the denominator:  "))
s=0
for j in range (1,n+1):
    z=(x**j)/j
    s=s+z
print("The sum of series is", s)
    

