##Separate each digit of a number

num= int(input("Enter the number: "))
temp=num
while(temp!=0):
    rem=temp%10
    print(rem)
    temp=temp//10