# Oprations on List

list = [1,3,5,7]
print(list)
print(type(list))
list.append(9)
print("after append " , list)
list.extend([11,13,15])
print("after extend " , list)
print("3rd to 6th", list[3:7])
print("Lists",list + list[3:7])
print("3rd to 6th for 3 times", list[3:7]*3)
list.insert(1,2)
print(list)
del list[1]
print(list)
