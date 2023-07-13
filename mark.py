#fuction to find average marks
marks=[55,89,68,90,50]
def find_average_marks(marks):
    sum_of_marks=sum(marks)
    total_subjects=len(marks)
    average_marks=sum_of_marks/total_subjects
    return average_marks
average_marks=find_average_marks(marks)
print("average mark is:",average_marks)
#calculate the grade and return it
def compute_grade(average_marks):
    if average_marks>=80:
        grade='A'
    elif average_marks>=60:
        grade='B'
    elif average_marks>=50:
        grade='c'
    else:
        grade='F'
    return grade
grade=compute_grade(average_marks)
print("your grade is:",grade)

    