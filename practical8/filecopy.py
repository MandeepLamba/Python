# Write Python script to copy contents of a file to another file and
# display the no. of lines ,words  copied.
# Also count no. of vowels and consonants.

try:
    file_1 = open('mix.txt','r')
    file_2 = open('mix_1.txt','w')
    vow = ['a','e','i','o','u']
    count_vowal=0
    count_conso=0
    for line in file_1:
        file_2.write(line.rstrip())
    file_1.seek(0)
    print(len(file_1.read().split()),'words and',end = ' ')
    file_1.seek(0)
    print(len(file_1.readlines()),'lines copied!')
    file_1.seek(0)
    for letter in file_1.read():
        if(letter.isalpha()):
            if(letter in vow):
                count_vowal+=1
            else:
                count_conso+=1
    print('Total', count_vowal ,'vowals and', count_conso,'consonents are copied!')
except Exception as e:
    print(e)