class Student:
   def __init__(self,name,roll_no,marks):
       self.name=name 
       self.roll_no=roll_no
       self.marks=marks
       self.result="Fail"
       if self.marks>=40:
          self.result="Pass"

   def result(self):
       return self.result

   def show(self):
        print(f"Name is {self.name} Roll no is {self.roll_no} Marks is {self.marks} Result is {self.result}")
       
   
tarun=Student("tarun",32,62)
deepak=Student("deepak",33,30)
tarun.show()
deepak.show()