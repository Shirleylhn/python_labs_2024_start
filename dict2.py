import json

# 读取现有的 student.json 文件
with open('student.json', 'r') as file:
    data = json.load(file)

# 获取学生列表
students = data['students']
print(students)

for stu in students:
    print(f"ID:{stu['id']}")
    print(f"grade math:{stu['grades']['math']}")

# 新记录
record = {'id': 3, 'name': 'Amily', 'age': 30, 'grades': {'math': 90, 'science': 80}}
students.append(record)

# 更新数据
data['students'] = students

# 将更新后的数据写回 student.json 文件
with open('student.json', 'w') as file:
    json.dump(data, file, indent=4)

# 验证写入是否成功
with open('student.json', 'r') as file:
    data_new = json.load(file)

students_new = data_new['students']
print(students_new)