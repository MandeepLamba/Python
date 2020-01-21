num=numcopy=int(input("Enter a Number: "))
sum = 0
while numcopy > 0:
    sum += (numcopy%10)**3
    numcopy //= 10
print("{} is a Armstrong Number :".format(num),sum == num)