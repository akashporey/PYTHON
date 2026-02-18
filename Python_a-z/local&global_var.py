# local & Global variable

x=100
y=200
def call():
    x=101
    y=201
    print(x)
    print(y)

print(x)
print(y)
call()
print(x)
print(y)
## We can't access the local member inside the Global area directly.
## By the help of reference adress and function name, 
    # we can excute local member globally inside the console.
print("_________________________________")

x=100
y=200
def call():
    global x
    global y
    x=101
    y=201
    print(x)
    print(y)

print(x)
print(y)
call()
print(x)
print(y)
## We can overwrite the global variable inside the local by using global keyword.