print("\n\n\t\t\t\tWelcome to GPA Calculator")
print("\tPlease enter your marks below")


bangla = int(input("\tBangla: "))
english = int(input("\tEnglish: "))
math = int(input("\tMath: "))
science = int(input("\tScience: "))


class Grade:

    def __init__(self, num):
        self.num = num

    def point(self):

        if self.num >= 80:
            return 5.00
        elif self.num >= 70:
            return 4.00
        elif self.num >= 60:
            return 3.50
        elif self.num >= 50:
            return 3.00
        elif self.num >= 40:
            return 2.00
        else:
            return 0.00
        

bangla_grade = Grade(bangla).point()
english_grade = Grade(english).point()
math_grade = Grade(math).point()
science_grade = Grade(science).point()

gpa = (bangla_grade + english_grade + math_grade + science_grade) / 4

print(f"\n\n\t\t\tYour GPA is: {gpa:.2f}\n")