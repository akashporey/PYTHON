## Factorial of each digit of input value

num= int(input("Enter the number: "))
temp=num

while(temp!=0):
    rem=temp%10
    fact=1
    temp2=rem
    while(rem!=0):
        fact=fact*rem
        rem=rem-1
    print(f"The factorial of {temp2} is: {fact}")
    temp=temp//10