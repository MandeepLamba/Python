dict_size = int(input("Enter Size of dict: "))
value_size = int(input("Enter Size of Value of dict: "))
dictionary={input("Key: "):[input("Value: ") for i in range(value_size)] for j in range(dict_size)}

# print(dictionary)

# dictionary = {'1':['a','b'], '2':['c','d'],'3':['e','f']}

# dup=dictionary

# while len(dup)!=0:
#     for key in dup.keys():
#         for el in dup.pop(key):
#             print(el)
        

# keys = dictionary.keys()
# for key in keys:
#     for i in range(len(dictionary.get(key))):
#         print(dictionary.get(key)[i],end=" ")
#         for j in range(len(dictionary.get(key))):
#             print(dictionary.get(key)[j])

# first =[]
# for i in keys:
#     first=dictionary.get(i)
#     break

# for j in range()

# it = iter(dictionary.values())
# print(type(it))
# print(next(it))
# print(next(it))



print(dictionary)

values=list(dictionary.values())
for i in values[0]:
    for j in values[1:]:
        for k in j:
            print(i,k)
