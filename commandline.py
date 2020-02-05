import sys
sum=0
for a in sys.argv[1:]:
    sum+=int(a)
print("Command Line Args are: ", sys.argv[1:],"\nSum: ",sum)