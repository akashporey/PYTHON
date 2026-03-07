

num= int(input("Entyer the number: "))
temp=num
sum=0
mul=1
while(temp!=0):
    rem=temp%10
    sum=sum+rem
    mul=mul*rem
    temp=temp//10
print(f"The digits sum of {num} is: {sum}")
print(f"The digits of multiplication of {num} is: {mul}")