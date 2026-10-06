MY_NAME="TARUN CHAUDHARY"

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, value):
        if value < 0 or value > 100:
            print("Invalid marks. Marks must be between 0 and 100.")
        else:
            self.__marks = value

    def get_marks(self):
        return self.__marks

    def grade(self):
        if self.__marks >= 80:
            return "A"
        elif self.__marks >= 60:
            return "B"
        elif self.__marks >= 40:
            return "C"
        else:
            return "Fail"

    def __str__(self):
        return f"Name: {self.name}, Marks: {self.__marks}, Grade: {self.grade()}"

s1 = Student(MY_NAME, 85)
s2 = Student("Rahul", 72)
s3 = Student("Priya", 38)

if __name__ == "__main__":
    print(s1)
    print(s2)
    print(s3)

    print("Trying to set marks to 150:")
    s1.set_marks(150)
    print(s1)