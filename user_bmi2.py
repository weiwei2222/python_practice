# 文本类型 str
# 数值类型 int float complex
# 序列类型 list tuple range
# 映射类型 dict
# 集合类型 set, frozenset
# 布尔类型 bool
# 空值类型 None
# 二进制类型 bytes, bytearray, memoryview

# 计算BMI=体重kg除以身高米的平方米

weight = int()
height = int()
while weight <= int():
    try:
        weight = float(input("input your weight (kg)："))
        if weight <= 0:
            print("please input a positive number!")
    except ValueError:
        print("please input a positive number!")

while height <= int():
    try:
        height = float(input("input your height (m)："))
        if height <= 0:
            print("please input a positive number!")
    except ValueError:
        print("please input a positive number!")


def user_bmi_count(weight,height):
    user_bmi = weight / height ** 2
    if user_bmi >= 28:
        print(f"Your BMI is {user_bmi :.2f} You are too fat! you need to lose your weight!")
    elif user_bmi >= 24:
        print(f"Your BMI is {user_bmi :.2f} Your weight are too high! try eat more health.")
    elif user_bmi >= 18.5:
        print(f"Your BMI is {user_bmi :.2f} You are very health.")
    elif user_bmi < 18.5:
        print(f"Your BMI is {user_bmi :.2f} You are too skinny.")
    return user_bmi


user_result = user_bmi_count(weight, height)
