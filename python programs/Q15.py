i=int(input("Enter the total quantity of product"))
if (i<10):
    p=i*120
elif (i>=10 and i<=99):
    p=i*100
else:
    p=i*70
print("Total cost is",p, end=' ')

