# string = input("Enter String: ")
string = "My name is mandeep"
print("Orignal String",string)
splited = string.split()
print("After Split: ",splited)
joined = "_".join(splited)
print("After join with '_': ",joined)
string=string.replace("mandeep", "Mandeep")
print('After replace: ',string)
print('In Upper Cases: ',string.upper())
print('In Lower Cases: ',string.lower())
print('Location of "name": ',string.find("name"))
print('Count of "e": {0}'.format(string.count('e')))
print(string.center(40, "_"))
print(string.ljust(40, "_"))
print(string.rjust(40, "_"))
print('Is Alphanumaric: ',string.isalnum())
print('Swaped: ',string.swapcase())
print('Substring: ',string[3:10])