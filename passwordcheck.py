pwd=input("> ")
countdigit=0
countsym=0
for c in pwd:
    if c.isdigit():
        countdigit+=1
    elif c in ('!','@','#','$','%','&','*'):
        countsym+=1

print(countdigit)
print(countsym)
print(len(pwd))