#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     02/09/2022
# Copyright:   (c) user 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
sum1=a+b+c
print(sum1)
if a==b:
    sum2=a+c
    print(sum2)
elif a==c:
    sum2=a+b
    print(sum2)
elif b==c:
    sum=a+b
    print(sum2)
else :
    sum2=a+b+c
    print(sum2)
x=input("enter a character:")
print("character is: " +x)
if x>=65 and x<=90:
    print("character is upper case : " +x)
elif x>=97 and x<=122:
    print("lowercase:"+x)
elif  x>=48 and x<=57:
    print("number: "+x)
else:
    print("special :" +x)
num1=int(input("Enter First number : "))
num2=int(input("Enter Second number : "))
num3=int(input("Enter Third number : "))
if num1<num2 and num1<num3:
    if num2<num3:
        x,y,z=num1,num2,num3
    else:
        x,y,z=num1,num3,num2
elif num2<num1 and num2<num3:
    if num1<num3:
        x,y,z=num2,num1,num3
    else:
        x,y,z=num2,num3,num1
else:
    if num1<num2:
        x,y,z=num3,num1,num2
    else:
        x,y,z=num3,num2,num1
print("Numbers in ascending order are : ",x,y,z)
height = float(input('Please enter your height input meters(decimals): '))
weight = int(input('Please enter your weight input kg: '))
bmi = weight/(height*height)

if bmi <= 18.5:
    print('Your BMI is', bmi,'which means you are underweight.')

elif bmi > 18.5 and bmi < 25:
    print('Your BMI is', bmi,'which means you are normal.')

elif bmi > 25 and bmi < 30:
    print('your BMI is', bmi,'overweight.')
elif bmi > 30:
    print('Your BMI is', bmi,'which means you are obese.')

else:
    print('There is an error with your input')
    print('Please check you have entered whole numbers\n'
              'and decimals were asked.')
a=input("what you want?:")
c=int(input("Enter First number : "))
b=int(input("Enter Second number : "))
if a=='sum':
    sum1=c+b
    print(sum1)
elif a=='product':
    pro=c*b
    print(pro)
elif a=='quotient':
    quo=c//b
    print(quo)
elif a=='remainder':
    rem=c%b
    print(rem)
a=input("enter your choice")
num=int(input("enter a number:"))
while a=='prime':
    for i in range(2,num):
        if(num%i==0):
            break
        else:
            print("is prime: " ,num)
    break
while a=='armstrong':
    add = 0
if num> 0:
    digit = num % 10
    add =add + (digit ** 3)
    num //= 10
if num == add:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
print("1)decimal to binary",'\n',"2)binary to decimal")
a=int(input("enter users choice"))
if (a==1):
    num=int(input("enter a  binary number"))
    d=0
    base=0
    l=len((str(num))
    for i in range(l):
        rem=num%10
        d=d+(rem*base)
        num=int(num/10)
        base=base*2
        print(d,"decimal equivalent")
elif (a==2):
    num=int(input("enter a  decimal number")
    binary=0
    temp=0
    rem=0
    while(num>0):
        rem=num%2
        num=int(num/2)
        binary=binary+(rem**temp)
        temp=temp*10
        print("binary of {x} is :{y}",format(x=num,y=binary))
    else:
        print("invalid")'''
def GCD_Loop( a, b):
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if (( a % i == 0) and (b % i == 0 )):
            gcd = i
    return gcd
x = int(input (" Enter the first number: ") )
y =int (input (" Enter the second number: "))
num = GCD_Loop(x, y)
print("GCD of two number is: ")
print(num)



