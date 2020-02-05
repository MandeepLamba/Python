total=0
for i in range(5):
    total+=int(input("Enter Marks in Subject {}: ".format(i+1)))
avg=total/5
if (avg>=90):
    print("Distinction")
elif (avg>=80):
    print("First Class")
elif (avg>=70):
    print("Second Class")
elif (avg>=60):
    print("Third Class")
else:
    print("Fail")