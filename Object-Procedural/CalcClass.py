class CalcClass:
    a = 0
    b = 0

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            return 0
        return self.a / self.b

    def pow(self):
        return self.a ** self.b
