# Create class Student that take 3 student marks and has a methid that give ouput its average

class Student:
    def __init__(self, name, listofmarks):
        self.name = name
        self.listofmarks = listofmarks

    def average(self):
        total = 0

        for eachval in self.listofmarks:
            total = total + eachval

        average = total / len(self.listofmarks)

        print("The average is:", average)


student1 = Student("Rahul", [10, 40, 34])
student1.average()