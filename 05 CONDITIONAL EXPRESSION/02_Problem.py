"""Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user."""

P=int(input("Enter Physics number: "))
E=int(input("Enter english number: "))
M=int(input("Enter math number: "))

T=((P+E+M)*100)/300

if(T>=40 and P>=33 and E>=33 and M>=33):
    print("The student has passed. Total percentage is: ",T)

else: 
    print("The student has failed. Total percentage is: ", T)