import Tarun_A4_B as T
import csv,json

#C1:TEXT FILE 
with open("students.txt", "w") as file:
    file.write(T.s1.name + "," + str(T.s1.get_marks()) + "\n")
    file.write(T.s2.name + "," + str(T.s2.get_marks()) + "\n")
    file.write(T.s3.name + "," + str(T.s3.get_marks()) + "\n")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

#C2:CSV FILE
with open("students.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["name", "marks"])
    writer.writerow([T.s1.name, T.s1.get_marks()])
    writer.writerow([T.s2.name, T.s2.get_marks()])
    writer.writerow([T.s3.name, T.s3.get_marks()])

with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

#C3:JSON FILE

students = [
    {
        "name": T.s1.name,
        "marks": T.s1.get_marks(),
        "grade": T.s1.grade()
    },
    {
        "name": T.s2.name,
        "marks": T.s2.get_marks(),
        "grade": T.s2.grade()
    },
    {
        "name": T.s3.name,
        "marks": T.s3.get_marks(),
        "grade": T.s3.grade()
    }
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)


with open("students.json", "r") as file:
    data = json.load(file)

for student in data:
    print(student["name"], student["grade"])
