# Write a program to store seven fruits in a list entered by the user.

Fruits = []

N1=input("Enter fruit name: ")
Fruits.append(N1)

N2=input("Enter fruit name: ")
Fruits.append(N2)

N3=input("Enter fruit name: ")
Fruits.append(N3)

N4=input("Enter fruit name: ")
Fruits.append(N4)

N5=input("Enter fruit name: ")
Fruits.append(N5)

N6=input("Enter fruit name: ")
Fruits.append(N6)

N7=input("Enter fruit name: ")
Fruits.append(N7)

print(Fruits)

# OR

Fruits = []

for i in range(7):
    Fruit=input("Enter Fruit name:")
    Fruits.append(Fruit)

print(Fruits)