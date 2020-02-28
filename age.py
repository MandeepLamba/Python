from datetime import date
# cdate=date.today()
day,month,year = [int(i) for i in input("Enter Date (dd-mm-yyyy): ").split("-")]
isleep = isvalid = True

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
        if day>31:
            isvalid = False
elif month in [4,6,9,11]:
        if day>30:
            isvalid = False
elif month==2:
    if isleep:
        if day>29:
            isvalid = False
    else:
        if day>28:
            isvalid = False
else:
    isvalid = False
if isvalid:
    print("Valid Date")
else:
    print("Invalid Date")

# if isvalid:
#     DOB = date(year,month,day)
#     ageyear = int((cdate - DOB).days / 365.2425)
#     agedays = int((cdate - DOB).days % 365.2425)
#     print("Age is {} years and {} days!".format(ageyear,agedays))
# else:
#     print("Date is not valid")
