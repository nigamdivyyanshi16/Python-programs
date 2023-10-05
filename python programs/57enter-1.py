while True:
    string = input("Enter a String to end the string write enter: ") 
    z=string.split()
    if (z[-1]!='enter'):
        continue
    else:
        break
count=0
k=string[0:-6]
print("String is",string[0:-6])
lst=list((string[0:-6]).split())
print("Number of words are",len(lst))
print("Number of characters are",len(string[0:-6]))
for i in range(len(string[0:-6])):
    if (k[i]>=chr(65) and k[i]<=chr(90) or k[i]>=chr(97) and k[i]<=chr(122)):
        count=count+1
num=count/255
per=num*100
print("percentage of alphanumeric characters are",per,"%")
