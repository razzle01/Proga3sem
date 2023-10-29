class Group:
    def __init__(self, group_id, name):
        self.group_id = group_id
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, student_id, name, birth_year, group):
        self.student_id = student_id
        self.name = name
        self.birth_year = birth_year
        self.group = group

    def __str__(self):
        return f"{self.name} ({self.birth_year})"

class many_to_many:
    def __init__(self, student_id, group_id):
        self.student_id = student_id
        self.group_id = group_id

# Создаем тестовые данные
group1 = Group(1, "А1")
group2 = Group(2, "Б1")

student1 = Student(1, "Иванов", 1998, group1)
student2 = Student(2, "Петров", 1997, group1)
student3 = Student(3, "Сидоров", 1999, group1)
student4 = Student(4, "Иваненко", 1996, group2)
student5 = Student(5, "Артемов", 1999, group2)

group1.add_student(student1)
group1.add_student(student2)
group1.add_student(student3)
group2.add_student(student4)
group2.add_student(student5)

groups = [group1, group2]
students = [student1, student2, student3, student4, student5]

many_to_many = [
    many_to_many(1, 1),
    many_to_many(2, 1),
    many_to_many(3, 1),
    many_to_many(4, 2),
    many_to_many(5, 2),
]

students_dict = {student.student_id: student for student in students}
groups_dict = {group.group_id: group for group in groups}

# Запрос 1
print("Задание 1")
for group in groups:
    if group.name.startswith('А'):
        print(group.name)
        for student in group.students:
            print(f"\t{student.name} {student.birth_year}")

# Запрос 2
print("\nЗадание 2")
max_birth_years = {}
for group in groups:
    max_year = max(student.birth_year for student in group.students)
    max_birth_years[group.name] = max_year

for group, year in max_birth_years.items():
    print((group, year))

# Запрос 3
print("\nЗадание 3")
for group in groups:
    print(group.name)
    for student in group.students:
        print(f"\t{student.name}")