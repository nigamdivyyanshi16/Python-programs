a=((23,5,7,4),(8,2,6,7),(10,13,1,38))
s=0
mean=0
me=0
for i in range(len(a)):
    for j in range(len(a[i])):
        s=s+a[i][j]
    mean=s/(j+1)
    print("mean element ",i+1,":",mean)
    me=me+mean
print("mean of means: ",me/3)
