T = int(input())
ss = [input() for i in range(T)]
m=[]
for s in ss:
    print(len(s))
    chars=list(set(s))
    mul=[i for i in chars if s.count(i)>1]
    for i in mul:
        m.append((len(s)-s[::-1].find(i)-2)-s.find(i))
    print(max(m))