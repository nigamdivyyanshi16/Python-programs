string = input("Please Enter a String : ")
ostring = ''
for i in range(len(string)):
    if(string[i] >= 'a' and string[i] <= 'z'): 
        ostring = ostring + chr((ord(string[i]) - 32)) 
    elif(string[i] >= 'A' and string[i] <= 'Z'):
        ostring = ostring + chr((ord(string[i]) + 32))
    else:
        ostring = ostring + string[i]
 
print("\nOriginal String", string)
print("The String After Toggling Case", ostring)
