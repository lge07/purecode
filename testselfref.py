# Testing reference to self

class Test:
    def __init__(self, a):
        self.a = a
    
    def getSelf(self):
        return self

x = Test(1)
print(x)
y = x.getSelf()
print(y)