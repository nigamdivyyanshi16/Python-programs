z=input("Enter an email id:")
m=z.split("@")

if (m[1]=='google.com'):
    print("The server is google")
elif (m[1]=='yahoo.com'):
    print("The server is yahoo")
elif (m[1]=='rediffmail.com'):
    print("The server is rediffmail")
elif (m[1]=='microsoft.com'):
    print("The server is microsoft")
elif (m[1]=='gmail.com'):
    print("The server is Gmail")
else:
    print("Sever error or server not found")




