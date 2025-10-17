class Student:
    def __init__(self, name, roll_no):  # Corrected constructor name
        self.name = name
        self.roll_no = roll_no
        print("Inside Constructor:")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
    def update_marks(self, marks):
        self.marks = marks
        print("\nInside Instance Method:")
        print(f"{self.name}'s Marks Updated to:", self.marks)
s1 = Student("Moin", 285)
s1.update_marks(180)
print("\nOutside of Class:")
print("Name (before):", s1.name)
s1.name = "Padmasri"
print("Name (after):", s1.name)
s1.update_marks(85)
print("Marks (outside):", s1.marks)
