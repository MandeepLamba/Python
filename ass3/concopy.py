try:
    file_1 = open('test1.txt','r')
    file_2 = open('test2.txt','w')
    for line in file_1:
        file_2.write(line.rstrip())
except Exception as e:
    print(e)
