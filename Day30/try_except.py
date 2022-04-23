try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["aaa"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError:
    print("That key does not exist.")
