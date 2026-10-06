def get_marks():
  try:
    marks=int(input("Enter the marks "))
    if marks<0 or marks>100:
       print("Marks must be between 0 and 100")
    else:
       if marks>=40:
          print("Pass")
       else:
          print("Fail")

  except ValueError:
        print("Please enter a number")



get_marks()