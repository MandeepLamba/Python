x = int(input("Enter a number: "))
sym=[')','!','@','#','$','%','^','&','*','(']
sum=x
while(sum>9):
    sum=0
    while(x>0):
        sum+=x%10
        x//=10
    x=sum
print("Sum =",sum,"Symbol =",sym[sum])