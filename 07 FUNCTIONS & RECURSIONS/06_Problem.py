# Write a python function which converts inches to cms.

def con(In) :
    if(In==0):
        return
    return In*2.54

print(con(int(input("Enter value in Inches: "))),end="")
print(" cm")
