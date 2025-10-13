# Write a program to print multiplication table of a given number using while loop.

N=int(input("Enter a number: "))
i=1
while(i<11):
    print(f"{N} x {i} = {N*i}")
    i+=1
