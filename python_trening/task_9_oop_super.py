class A:
    def __init__(self, x = 10):
        self.x = x

class B(A):
    def __init__(self, y, x = 100):
        super().__init__(x)
        self.y = self.x + 50

sum = B(1)
print(sum.y)