class Student:
    def __init__(self, name, roll_no, age, course, grade):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.course = course
        self.grade = grade

student1 = Student("Mohammed Moin",285,19,"Computer Science","A")

print("Name:", student1.name)
print("Roll No:", student1.roll_no)
print("Age:", student1.age)
print("Course:", student1.course)
print("Grade:", student1.grade)
