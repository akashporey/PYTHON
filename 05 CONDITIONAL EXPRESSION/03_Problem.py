'''A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.'''

sp1 = "Make a lot of money"
sp2 = "buy now "
sp3 = "subscribe this" 
sp4 = "click this"

c = input("Enetr your comment: ")

if((sp1 in c) or (sp2 in c) or (sp3 in c) or (sp4 in c)) :
    print("Your comment is a spam.")

else:
    print("Your comment is not a spam.")