#Dynamic memory allocation : same literals value does not create extra cetridge

x=y=z=100
print(x, id(x))
print(y, id(y))
print(z, id(z))