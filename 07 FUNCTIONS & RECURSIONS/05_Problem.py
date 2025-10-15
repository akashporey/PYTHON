'''Write a python function to print first n lines of the following pattern:
***
**     - for n = 3           
*                       '''

def pattern(s) :
    if(s==0) :
        return
    print("*" * s)
    pattern(s-1)

pattern(int(input("Number of lines : ")))