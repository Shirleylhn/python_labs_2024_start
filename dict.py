import json
fruits = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "orange": "orange"
}

print(fruits)

first_item = next(iter(fruits.items()))
print(first_item)

grape_color = fruits["grape"]
print(grape_color)
 

with open('student.json', 'r') as file:
    data = json.load(file)
    
student = data['students']
print(student)

for stu in student:
    print(f"ID:{stu['id']}")
    print(f"grade math:{stu['grades']['math']}")

record = {'id':3,'name':'Amily','age': 30,'grades': {'math': 90, 'science': 80}}
student.append(record)
data['students'] = student
with open('student.json', 'w') as file:
    json.dump(data, file)

with open('student.json', 'r') as file:
    data_new = json.load(file)

student_new = data_new['students']
print(student_new)