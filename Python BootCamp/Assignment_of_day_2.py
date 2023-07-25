'''
                                         Title: "Student Grading Program"



 #Problem statement description:

               You are tasked with creating a simple student grading program using Python. 
               The program should take input from the user for the marks obtained by
                a student in a subject and then calculate and display the grade.
                
                
Solution :
'''
#Taking Input From User For Marks Obtained By Student In A Subject And Calculating

mark = int(input("Enter your number: "))
if mark >= 90:
    grade="A+"
elif mark >= 80 and mark <= 89:
    grade="A"
elif mark >= 70 and mark <= 79:
    grade="B"
elif mark >= 60 and mark <= 69:
    grade="C"
elif mark >= 50 and mark <= 59:
    grade="D"
else:
    grade="Fail"
    
print(grade)
