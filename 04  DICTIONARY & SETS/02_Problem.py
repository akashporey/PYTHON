""" Write a program to input eight numbers from the user and display all the 
unique numbers (once).  """

s= set()

n= input("Enter number: ")
s.add(n)

n= input("Enter number: ")
s.add(n)

n= input("Enter number: ")
s.add(n)

n= input("Enter number: ")
s.add(n)

n= input("Enter number: ")
s.add(n)

n= input("Enter number: ")
s.add(n)

n= input("Enter number: ")
s.add(n)

print(s)

# OR

s= set()

for i in range(7) :
    n=input("Enter number: ")
    s.add(n)

print(s)