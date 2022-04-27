import pandas

students_data = pandas.read_csv("students_scores.csv")
all_scores = students_data.score.to_list()

students_grade = []
for score in all_scores:
    if score >= 90:
        grade = 'A'
        students_grade.append(grade)
    elif score >= 80:
        grade = 'B'
        students_grade.append(grade)
    elif score >= 70:
        grade = 'C'
        students_grade.append(grade)
    elif score >= 60:
        grade = 'D'
        students_grade.append(grade)
    else:
        grade = 'F'
        students_grade.append(grade)


def evaluate_student(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# 方法一
print(students_grade)
students_dict = students_data.to_dict()
new_students_data = pandas.DataFrame(students_dict)
new_students_data["grade"] = students_grade
# 方法二
# new_students_data = students_data
# new_students_data["grade"] = students_grade

# 方法三
# new_students_data["grade"] = new_students_data["score"].map(evaluate_student)

print(new_students_data)
new_students_data.to_csv("new_students.csv", index=False)
