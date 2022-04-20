# with open("/Users/weiweilin/Downloads/test.txt") as file:
#     contents = file.read()
#     print(contents)

with open("../../../Desktop/test222.txt") as file:
    contents = file.read()
    print(contents)

with open("../../test.txt") as file:
    contents = file.read()
    print(contents)

# "a" is read and write more in the end of file
with open("/Users/weiweilin/Downloads/test.txt", mode="a") as file:
    file.write("New text. This is test")
# Writing to Files

with open("my_file.txt", mode="w") as file:
    file.write("New text.222")

# Opening a File that doesn't exit in write mode will create it from scratch

with open("file_that_doesnt_exist.txt", mode="w") as file:
    file.write("New text.Haha")
