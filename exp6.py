string = "AABCAAADA"
k=3
for i in range(0,len(string),k):
    s=""
    for c in string[i:i+k]:
        if c not in s:
            s+=c
    print(s)