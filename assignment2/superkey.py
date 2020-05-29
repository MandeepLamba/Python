class A:
    a=4
    def __init__(self):
        self.a=8
class B(A):
    def __init__(self):
        super().__init__()

print(B.a)
b= B()
print(b.a)