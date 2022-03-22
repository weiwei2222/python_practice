# format字符串格式化
# format() 方法允许您格式化字符串的选定部分。
# 有时文本的一部分是你无法控制的，也许它们来自数据库或用户输入？
# 要控制此类值，请在文本中添加占位符（花括号 {}），然后通过 format() 方法运行值：

# name = "小王"
# year = "虎"
# message_content = f"""金{year}贺岁，欢乐祥瑞。金{year}敲门，五福临门。给{name}及家人拜年啦！新春看了，{year}年大吉!"""
# print(message_content)


gpa_dict = {"lily": 3.195, "mike": 3.145, "xing": 3.335, "kate": 3.234}
for name in gpa_dict:
    # score = gpa_dict[name]
    # print("{0} hello,your score is {1}".format(name,score))
    print(f"{name} hello,your score is {gpa_dict[name]:.2f}")
