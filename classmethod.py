class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
            print(f"name: {self.name},age: {self.age}")

student1=student("Moin",19)
student2=student("Akhil",20)
student1.display_info()
student2.display_info()