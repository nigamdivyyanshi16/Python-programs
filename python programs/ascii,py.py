ch=input("Enter a character")
if (ch>='A' and ch<='Z'):
    print(ch,"is uppercase")
elif  (ch>='a' and ch<='z'):
    print(ch,"is lowercase")
elif (ch>=str(0) and ch<=str(9)):
    print(ch,"is digit")
else:
    print(ch,"is special character")
