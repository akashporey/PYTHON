

num= int(input("Enter the number: "))
temp=num
fact=1
while(temp!=0):
    fact=fact*temp
    temp=temp-1
print(f"The factorial of {num} is: {fact}")