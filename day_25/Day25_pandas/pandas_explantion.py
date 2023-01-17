# with open("weather_data.csv") as data:
#     content = data.readlines()
#     print(content)

# import csv
#
# with open("weather_data.csv") as data:
#     content = csv.reader(data)
#     temperature = []
#     for row in content:
#         print(row[1])
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")

# print(data)

# there are 2 types in pandas : dataframe(2dimensional) and series(1dimensional)

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
average = data["temp"].mean()
print(average)

# to get a data
max_temp = data["temp"].max()
# above and below syntax are same only
maxtemp = data.temp.max()
print(max_temp)
print(maxtemp)

# to get a row from the dataframe
row = data[data.day == 'Monday']
print(row)
# to get a maximum temp row data
row_temp = data[data.temp == data.temp.max()]
print(row_temp)

monday = data[data.day == 'Monday']
print(monday.temp)

