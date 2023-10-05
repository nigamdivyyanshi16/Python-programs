l1=[]
st=" "
m=input("Enter a message:")
key=int(input("Enter the key value:"))
l=len(m)
for i in range (l):
    ch=ord(m[i])
    ch=ch+key
    l1.append(chr(ch))
print("Message before encryption is\n",m)
print("Message after encryption is\n",st.join(l1))
