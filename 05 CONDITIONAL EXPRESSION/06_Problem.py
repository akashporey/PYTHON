"""Write a program to calculate the grade of a student from his marks from the
following scheme:
90-100 => Ex
80-90 => A
70-80 => B
60-70 => C
50-60 => D
<50   => F                        """

M=int(input("Enter the student's marks: "))

if(M>=90 and M<=100) :
    print("Student's grade is Execellent")
    
elif(M>=80 and M<=90) :
    print("Student's grade is A")
    
elif(M>=70 and M<=80) :
    print("Student's grade is B")
    
elif(M>=60 and M<=70) :
    print("Student's grade is C")
    
elif(M>=50 and M<=60) :
    print("Student's grade is D")
    
elif(M<50) :
    print("Student's grade is F")
    
else:
    print("Wrong input")