
# with open("weather_data.csv") as weather_data:
#     data =weather_data.readlines()
#
# print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = list(csv.reader(data_file))

#     temperature = []
#     for row in data[1:]:
#         temperature.append(int(row[1]))
#
#
#     print(temperature)

import pandas as pd
#
# data =pd.read_csv("weather_data.csv")
# print types of pandas
# print(type(data))
# print(type(data["temp"]))
#
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# # temp_list =data["temp"].to_list()
# # temp_avg = sum(temp_list)/len(temp_list)
# temp_avg = data["temp"].mean()
# print(temp_avg)
#
# temp_max = data["temp"].max()
# print(temp_max)
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)

#Get data in row
# print(data[data.day == "Monday"])
# print(data[data["temp"] == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp * 9/5 + 32)
#
# #Create a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": {76, 56, 65}
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("weather_data.csv", index=False)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_data = data["Primary Fur Color"]
print(fur_data.value_counts())




