string = input("Enter a String : ") 
result=''
for i in string:  
    if i not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        result += i 
print("String after removing the vowels :",result)
