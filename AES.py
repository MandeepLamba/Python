text="PRESENCE OF ALL IS REQUIRED"
key=[]
for c in text:
    key.append(str(c)+" : "+str(hex(ord(c)).lstrip("0x")))

for i in key:
    print(i)
