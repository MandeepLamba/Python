month = int(input("Enter month number: "))
year = int(input("Enter year: "))
isleep = True
if (year%4)==0:
    if (year%100)==0:
        if (year%400)==0:
            isleep = True
        else:
            isleep = False
    else:
        isleep = True
else:
    isleep = False

if month in [1,3,5,7,8,10,12]:
        print("Number of days 31")
elif month in [4,6,9,11]:
        print("Number of days 30")
elif month==2:
    if isleep:
        print("Number of days 29")
    else:
        print("Number of days 28")
else:
    print("Invalid Month!")