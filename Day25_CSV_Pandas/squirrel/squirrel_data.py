import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_gray = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
squirrel_gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
squirrel_black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
squirrel_cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
print(squirrel_gray_count)
print(squirrel_black_count)
print(squirrel_cinnamon_count)

squirrel_dict = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [squirrel_gray_count, squirrel_black_count, squirrel_cinnamon_count],
}
print(squirrel_dict)

df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_count.csv")
