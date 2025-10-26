# Write a python program using function to convert Celsius to Fahrenheit.

def convert(C):
    F= (9*C+160)/5
    return F

C=int(input("Enter temp in Celsius: "))
print(f"Temp in Fahrenheit: {convert(C)}")

""