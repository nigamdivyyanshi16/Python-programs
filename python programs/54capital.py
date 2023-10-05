string = input("Enter a String : ") 
z=string.split()
result=""
for i in range (len(z)):
    for j in range (len(z[i])):
        if (j==0):
            string=z[i][j].upper()
        else:
            string+=z[i][j]
    z[i]=string
for j in z:
    result+=j+" "
print("output is",result)

