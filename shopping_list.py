# 学习list列表, list是可变的，list用[]符号。不可变的有字符串str，整数int，浮点数float，布尔bool
# Python 编程语言中有四种集合数据类型：
# 列表 List  是一种有序和可更改的集合。允许重复的成员。list用[]符号
# 元组 Tuple 是一种有序且不可更改的集合。允许重复的成员。Tuple用()符号
# 集合 Set 是一个无序和无索引的集合。没有重复的成员。set用{}符号
# 词典 Dictionary 是一个无序，可变和有索引的集合。没有重复的成员。字典用{}符号

shopping_list = ["potato","milk","eggs",[]]
shopping_list.append("skin care")
shopping_list.append("snack")
shopping_list.remove("skin care")
shopping_list[2] = str(len("tomato"))
print(shopping_list)
print(type(shopping_list))
print(len(shopping_list))
print(max(shopping_list))
print(min(shopping_list))
print(sorted(shopping_list))