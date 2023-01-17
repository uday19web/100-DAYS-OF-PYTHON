import pandas

data = pandas.read_csv("Squirrel_Data.csv")
print(type(data))
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_count)
print(red_count, black_count)

# to construt dataframe
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count]
}
# first need to convert as dataframe
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")