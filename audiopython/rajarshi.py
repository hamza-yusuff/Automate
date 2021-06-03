class student:
    clg = 'xyz' #class variable

    def __init__(self,name,rollno):# __init__() method is called the constructor of the class
        # Attributes
        self.name = name # class level scope variable
        self.rollno = rollno # class level scope variable

    def display(self): #method of my class
        print("Student name:", self.name)
        print("Student rollnumber is :", self.rollno)
        print("college:",student.clg)

# object1
student1 = student("Evan", 73)
student1.display()

# object2
student2 = student("Ivan", 43)
student2.display()

print(student1.name)# object level scope variable
print(student2.name)# object level scope variable
