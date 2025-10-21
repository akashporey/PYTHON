def greet():
    print("Good Day")

greet()
print("Thank You")
greet()
print("Thank You")
greet()
print("Thank You")

print("\n")

def greet(name,ending="Thank You"): #default ending if not mention later
    print("Good day",name,"\n",ending)

greet("Akash", "Thanks")

""