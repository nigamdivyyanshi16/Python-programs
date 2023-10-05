m=input("Enter a message:")
c=input("Enter a character to check:")
for i in range(len(m)):
    if c in m:
        loc=i
if c in m:
    print(c,"character is present at index",(loc-1))
    

