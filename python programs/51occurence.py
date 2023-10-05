m=input("Enter a message:")
c=input("Enter a character to check:")
count=0
for i in range(len(m)):
    if (m[i]==c):
        count+=1
print("Character occured",count,"times")
    

