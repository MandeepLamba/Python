import array as arr
sumodd=sumeven=0
print("Enter Number:\r") 
a = arr.array('i',[int(input(">>")) for j in range(6)])
for i in range(6):
    if a[i]%2==0:
        sumeven+=a[i]
    else:
        sumodd+=a[i]
print("Sum of Even numbers: {}".format(sumeven))
print("Sum of odd numbers: {}".format(sumodd))
