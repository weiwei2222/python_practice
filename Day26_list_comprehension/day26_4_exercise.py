# new_dict = {new_key:new_value for (key,value) in list}
# new_dict = {new_key:new_value for (key,value) in dict.item() if test}
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

# -------------------------------------
student_dict = {
    "student": ["Mike", "James", "Lily"],
    "score": [56, 76, 98]
}
# for (key, value) in student_dict.items():
#     print(key)
import pandas

student_date = pandas.DataFrame(student_dict)
print(student_date)
# for (student, score) in student_date.items():
#     print(score)

# for (index, row) in student_date.iterrows():
#     print(row.score)

# for (index, row) in student_date.iterrows():
#     if row.score >= 60:
#         print(row.student)

passed_students = {row.student: row.score for (index, row) in student_date.iterrows() if row.score >= 60}
print(passed_students)
