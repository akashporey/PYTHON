## Sum of each digits of the number

num= int(input("Entyer the number: "))
temp=num
sum=0
while(temp!=0):
    rem=temp%10
    sum=sum+rem
    temp=temp//10
print(f"The digits sum of {num} is: {sum}")