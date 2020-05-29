# Write a Python program to find the longest word in a text file whose name is entered by the user

filename = input("Enter Filename: ")
try:
    words=open(filename,'r').read().split()
    maxlenght = max([len(word) for word in words])
    print('Words with maximum lenght:',[word for word in words if(len(word)==maxlenght)])
except Exception as e:
    print(e)