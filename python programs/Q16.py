s=int(input("Enter your salary"))
i=0
if (s<=150000):
    print("No tax has to be paid")
elif (s>150000 and s<=300000):
    i=0.1*s
elif (s>300000 and s<=500000):
    i=0.2*s
else:
    i=0.3*s
print("Interest amount = ", i)
print("Salary after deducting interest = ", (s-i))
