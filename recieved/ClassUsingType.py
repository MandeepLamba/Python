''' we can define a class A with

type(classname, superclasses, attributedict)
When we call "type", the call method of type is called. The call method runs two other methods: new and init:

type.__new__(typeclass, classname, superclasses, attributedict)

type.__init__(cls, classname, superclasses, attributedict)
The new method creates and returns the new class object, and after this the init method initializes the newly created object.
'''
class Robot(object):

    counter = 0

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        return "Hello, I am " + self.name


def Rob_init(self, name):
    self.name = name

Robot2 = type("Robot2", (), {"counter":0, "__init__": Rob_init, "sayHi": lambda self,age: "Hi, I am " + self.name+ " " +str(age)})

x = Robot2("Marvin")
print(x.name)
print(x.sayHi(10))
x.counter=30
print(x.counter)

y = Robot("Mary")
print(y.name)
print(y.sayHello())

print(x.__dict__)
print(y.__dict__)
