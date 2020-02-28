name = input("\nEnter name: ")
symbol = ['!','@','#','$','%','^','&','*','(',')']
key=''
#First Key
sum=0
for i in range(len(name)):
    sum+=i
while sum>9:
    temp=0
    for i in range(len(str(sum))):
        temp+=i
    sum=temp
print(sum)
key += symbol[sum]

#Second Key
evenchar = [c for c in name[::2]]
evenchar.sort()
key += evenchar[0]

#Third Key
namelen = len(name)
while namelen>9:
    temp=0
    list = ([int(n) for n in str(namelen)])
    for n in list:
        temp+=n
    namelen=temp
key+=str(namelen)

#Fourth Key
oddchar = [c for c in name[1::2]]
oddchar.sort()
key+=str(oddchar[-1])

#Final Key
print("Key is: ",key)