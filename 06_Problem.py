""" Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.     """


a = {}

for i in range(4) :
    lang=input("Enter the language name: ")
    names=input("Enter friend names: ")
    a.update({names:lang})

print(a) 