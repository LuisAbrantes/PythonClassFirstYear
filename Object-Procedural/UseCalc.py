from CalcClass import CalcClass

print("-" * 10)
calc1 = CalcClass(1, 2)
print(calc1.add())
print(calc1.sub())
print(calc1.mul())
print(calc1.div())
print(calc1.pow())

print("-" * 10)
calc2 = CalcClass(10, 20)
print(calc2.add())
print(calc2.sub())
print(calc2.mul())
print(calc2.div())
print(calc2.pow())

print("-" * 10)
calc3 = CalcClass(10, 0)
print(calc3.add())
print(calc3.sub())
print(calc3.mul())
print(calc3.div())
print(calc3.pow())
