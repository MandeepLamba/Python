marks = int(input("Enter marks(1-100)"))

if marks>90:
    print("Grade A+")
elif marks>80:
    print("Grade A")
elif marks>70:
    print("Grade B+")
elif marks>60:
    print("Grade B")
elif marks>50:
    print("Grade C+")
elif marks>40:
    print("Grade C")
else:
    print("Failed!")