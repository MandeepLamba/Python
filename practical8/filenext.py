# Write a Python program to display all the odd lines from a file and then all the even numbers from the same file.
try:
    file = open('mix.txt','r')

    lines = file.readlines()

    for i in range(1,len(lines),2):
        print('Line number ',i+1,":",lines[i].rstrip())

    file.seek(0)
    print("Even Numbers: ", end = " ")
    for i in file.read().split():
        if(i.isnumeric()):
            if(int(i)%2==0):
                print(i,end = ' ')
except Exception as e:
    print(e)