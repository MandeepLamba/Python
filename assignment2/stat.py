class A:
   a=4
   def __init__(self):
       print("Object Created!")
       
 
#Assessing using Class name 
print(A.a)
 
#Assessing using object
b= A()
print(b.a)