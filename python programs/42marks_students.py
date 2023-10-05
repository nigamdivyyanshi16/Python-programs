tup=()
for i in range(1,6):
    print("enter the marks for student ",i)
    sub1=int(input("enter the marks for subject 1:"))
    sub2=int(input("enter the marks for subject 2:"))
    sub3=int(input("enter the marks for subject 3:"))
    tup=tup+((sub1,sub2,sub3),)
print(tup)
