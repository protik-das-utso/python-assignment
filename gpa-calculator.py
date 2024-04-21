print("\t\t\tWelcome to GPA Calculator")

def grade(sub_name):
    
    while True:
        try:
            grade = int(input(f"\t{sub_name} : "))
            
            if 0<= grade <= 100:
                return grade
            else:
                print("\t\tEnter a correct number between 0 and 100.")
        except:
              print("\t\tEnter a valid integer.")


bangla = grade("Bangla")
english = grade("English")
math = grade("Math")
science = grade("Science")


sum = bangla + english + math + science
avg = sum/4


if avg >= 91 and avg <= 100:
    gpa = "A+"
elif avg >= 81:
    gpa = "A"
elif avg >= 71:
    gpa = "B"
elif avg >= 61:
    gpa = "C"
elif avg >= 41:
    gpa = "D"
elif avg >= 0:
    gpa = "F"


print(f"\n\t\t\tYour GRADE is - \"{gpa}\"\n")