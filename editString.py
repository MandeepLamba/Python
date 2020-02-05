str = input("Enter String: ")
str2=""
for c in str:
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        str2+='z'
    else:
        str2+=c
print("Output: "+str2)