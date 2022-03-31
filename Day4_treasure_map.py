# row1 = ["a","b","c"]
# row2 = ["d","e","f"]
# row3 = ["g","h","i"]
# map = [row1, row2, row3]
#
# print(f"{row1}{row2}{row3}")
#
# print(map[2][0])
#
#
# numbers = [2,3]
#
# get1 = numbers[0]
# get2 = numbers[1]
#
# print(get2)


row1 = ["⬜️️","⬜️️","⬜️️"]
row2 = ["⬜️️","⬜️️","⬜️️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "😻"

map[vertical - 1][horizontal - 1] = "😻"

print(f"{row1}\n{row2}\n{row3}")

