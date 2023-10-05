#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      divyanshi nigam
#
# Created:     25-07-2022
# Copyright:   (c) HP 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""superhero=input("who is your superhero?")
print(superhero)
oldage=input("enter your old age:")
newage=int(oldage)+2
print(newage)
number=18
print(float(number))
first=input("first number is:")
second=input("second number is:")
sum=int(first)+int(second)
print("the sum is : " + str(sum))
name="tony stark"
print(name.upper())
print(name.lower())
print(name)
print(name.find('s'))
print(name.find("stark"))
print(name.find('S'))
name="tony stark"
print(name.replace("stark","Ironman"))
print(name)
print("T" , "M")
print('t' in name)
print('T' in name)
print(" " in name)
print(5*3)
print(5+3)
print(5/2)
print(5//2)
print(5%2)
print(5**2)
print(3==2)
print(3>2)
print(3!=3)
print(3>2 or 3==2)
print(3>2 and 2>56)
print(not 2>3)
age =19
if age>=18:
    print("adult")
    print("vote")
print("thanks")
age =2
if age>=18:
    print("adult")
    print("vote")
elif age<18 and age>3:
    print("you are in school")
else:
    print("child")
#calculator
print("welcome to divyanshi's calculator")
a=input("first number")
operator=input("enter operator(+,/,-,*):")
b=input("second number")
a=int(a)
b=int(b)
if operator =="+":
    print(a+b)
elif operator =="/":
    print(a/b)
elif operator =="-":
    print(a-b)
elif operator =="*":
    print(a*b)
else:
    print("invalid")
numbers=range(10)
print(numbers)
i=1
while i<=20:
    print(i)
    i=i+1
i=1
while i<=5:
    print(i* "  * ")
    i=i+1
for item in range(10):
        print(item+1)

print(input("good afternoon"))"""
name=input("enter name")
date=input("enter date")
letter =  '''
dear<name>
you are good.
<|date|>
'''
print=(letter.replace('<name>',name).replace('<|date|>',date))
