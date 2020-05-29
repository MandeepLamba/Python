# 1) Write Python code to read only numbers from a file named “mix.txt”
# and store it into an Array. In the last, print all the numbers along
#  with the number of vowel in the file.
try:
    file = open('mix.txt','r')
    uid=[]
    vow = ['a','e','i','o','u']
    count_vowal=0
    for word in file.read().split():
        if word.isnumeric():
            uid.append(word)
        else:
            for letter in word:
                if letter in vow:
                    count_vowal+=1
    print("UID's: " , uid)
    print("Total Vowals: ", count_vowal)
except Exception as e:
    print(e)