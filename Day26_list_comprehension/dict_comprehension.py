# new_dict = {new_key:new_value for (key,value) in list}
# new_dict = {new_key:new_value for (key,value) in dict.item() if test}
import random

names = ["Mike", "Beth", "Lily", "Freddie", "Caroline"]
# students_scores = {}
# for student in names:
#     students_scores[student] = random.randint(1, 100)

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
