import json


data = {
    "students": ["Tarun", "Rahul", "Manish"]
}

with open("batch.json", "w") as file:
    json.dump(data, file)


with open("batch.json", "r") as file:
    data = json.load(file)


data["students"].append("Priya")


with open("batch.json", "w") as file:
    json.dump(data, file)


print("Final list:", data["students"])
print("Number of names:", len(data["students"]))