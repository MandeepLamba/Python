num = int(input("Enter a Number: "))
isPrime = True
for i in range(num-1,1,-1):
    if num%i==0:
        isPrime=False
if isPrime:
    print("{} is a Prime Number.".format(num))
else:
    print("{} is not a Prime Number.".format(num))