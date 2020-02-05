from datetime import date

todaydate=date.today()
day,month,year = [int(i) for i in input().split(".")]

try:    
    DOB = date(year,month,day)
    
    age = (todaydate - DOB).days
    ageyear = int( age / 365.2425)
    agedays = int(age % 365.2425)
    ageweeks = int(age / 7)
    
    print("Age is {} years and {} days!\n".format(ageyear,agedays))
    print("You lived total {} days or we can say {} weeks.\n".format(age,ageweeks))
    
except:
    print("Invalid date!")