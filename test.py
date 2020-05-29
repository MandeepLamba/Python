N = int(input())
print(1)
n = 3
for num in range(n,N + 1):  
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
               break  
        else:
           print(n)
           n=n+num

