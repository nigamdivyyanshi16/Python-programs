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



