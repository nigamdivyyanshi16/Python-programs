string = input("Enter the string: ")
length = 0   
w = ''
result=''
for word in string.split():
    if(len(word) > length):
            length = len(word) 
            w = word
for i in w:  
    if i not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'): 
        result += i
final=len(result)
print("Longest word is", w,"with consonants",final)


