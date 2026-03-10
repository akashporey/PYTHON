

num= int(input("Enter the number: "))
temp=num
length=0
while(temp!=0):
    rem= temp%10
    length=length+1
    temp=temp//10
print(f"The length of {num} is: {length}")