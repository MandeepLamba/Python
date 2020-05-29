string = input("Enter String: ")
l,u=0,0
for c in string:
    if(c.isupper()):
        u+=1
    elif(c.islower()):
        l+=1
print("Upper Cases: ",u,"\nLower Cases: ",l)
