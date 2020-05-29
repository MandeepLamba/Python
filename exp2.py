# size=5

# for i in range(1-size,size):
#     ls=[chr(j) for j in range(97+size-1,97+abs(i)-1,-1)]
#     ls.extend(ls[::-1][1:])
#     print("-".join(ls).center(size*4-3,"-"))

sn="132 456 Wq  m e"
st=sn.split()
for s in st:
    print(s,s[0].upper()+s[1:])
    sn=sn.replace(s,s[0].upper()+s[1:])
print(sn)
