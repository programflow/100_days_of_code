
# with open("weather_data.csv") as weather_data:
#     data =weather_data.readlines()
#
# print(data)

import csv

with open("weather_data.csv") as data_file:
    data = list(csv.reader(data_file))
    temperature = []
    for row in data[1:]:
        temperature.append(int(row[1]))


print(temperature)
