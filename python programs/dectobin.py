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
    else:
          print("invalid input")
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
        print("invalid")

