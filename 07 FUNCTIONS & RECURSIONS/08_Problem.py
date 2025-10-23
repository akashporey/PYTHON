# Write a python function to print multiplication table of a given number.

def mul_table(n):
    if(n==0):
        return
    print(f"Multiplication table of {n} is: ")
    for i in range(1,11):
        print(n, "X", i, "=", n*i)
        i+=1


mul_table(int(input("Enter a number: ")))

