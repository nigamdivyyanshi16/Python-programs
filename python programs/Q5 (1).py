p=int(input("Enter the principle amount:"))
r=int(input("Enter the rate in percentage:"))
t=int(input("Enter the time in years:"))
print("for compound interest")
n=int(input("Enter frequency for compound interest:"))
s=(p*r*t)/100
asi=p+s
a=p*(1+(r/n))**(n*t)
c=a-p
print("Simple interest is: ",s)
print("Amount of simple interest is:",asi)
print("Compound interest is: ",c)
print("Amount of compound interest is:",a)
