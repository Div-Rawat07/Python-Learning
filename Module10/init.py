#  Init Constructor  -->> Type of Normal Constructor  -->> Runs Automatically whenever the object is created
class Student:
    schoolName = "ABC School"
    def __init__(self , name , course):
        # print("Whenever a new object is created i am called automatically")

        # Assigning 
        self.name = name
        self.course = course

        # print(self.name)
        # print(self.course)

    #  Method
    def hello(self):
        print("Hellooo Guyssss")


Student1 = Student("Rahul" , "Btech")  # Init method will be called
print("Student1 Name: " ,Student1.name)
print("Student1 Course: " ,Student1.course)
Student1.hello()

Student2 = Student("Anjali" , " BSC" )
print("Student2 Name: ", Student2.name)
print("Student2 Course: " ,Student2.course)

