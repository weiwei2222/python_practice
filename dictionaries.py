# 词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。字典用{}符号

my_contacts = {"Randy": 123345, "Weiwei": 125645, "Mom": 573345, "Dad": 1235667}
my_contacts["lily"] = 234555
# 字典中嵌套字典
my_contacts["kelly"] = {"friend": "hhhh"}
del my_contacts["Dad"]

# 找到某个字典，必须先找到key
print(my_contacts["Mom"])

search = input("input contacts name:")
if search in my_contacts:
    print(search + " number is " + str(my_contacts[search]))
else:
    print("there is no " + search + " number")
