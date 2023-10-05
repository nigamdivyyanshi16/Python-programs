x=int(input("Enter the value"))
a=int(input("Enter the number of terms"))
s1=0
s2=0
for i in range (1,a+1):
    if (i%2==0):
        s1=s1+(x**i)
    else:
        s2=s2+((-x)**i)
print("the sum of series is:",s1+s2)
