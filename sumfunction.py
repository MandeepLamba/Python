
def do_plus(a,b):
    if(type(a)==type(b)==int or type(a)==type(b)==str):
        print(a+b)
    else:
        print("Parameters should be of type int or string!")

V1= input("Enter First Parameter: ")
V2= input("Enter Second Parameter: ")
try:
    do_plus(eval(V1),eval(V2))
except:
    do_plus(V1,V2)
    