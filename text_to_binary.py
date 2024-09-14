text=input("Enter the text to be converted: ")
string=''
for x in text:
    temp=hex(ord(x))
    print(" ")
    string=string+str(temp)+" "


print(string)

