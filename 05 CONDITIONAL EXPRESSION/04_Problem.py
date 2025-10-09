'''Write a program to find whether a given username contains less than 10
characters or not.'''

u_n=input("Type your username: ")

L=len(u_n)
if(L<10):
    print(f"Username contains less than 10 characters. Username has {L} characters.")

elif(L==10):
    print(f"Username contains 10 characters.")

else:
    print(f"Username comtains more than 10 characters. Username has {L} characters.")
