class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
s1 = Student("Ali", 20)
s2 = Student("Sara", 22)
s1.display_info()
s2.display_info()

