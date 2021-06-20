# with open('weather_data.csv', mode='r') as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv', mode='r') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data)) # <class 'pandas.core.frame.DataFrame'>
# print(type(data['temp'])) # class 'pandas.core.series.Series'>

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()

# avg_temp = sum(temp_list) / len(temp_list)
# print(f"Average Temperature is: {round(avg_temp, 2)}")

#                              This does the same as the above
# print(f"Average Temperature is: {round(data['temp'].mean(), 2)}")
# #  Get the Min and Max
# print(f"Max Temperature is: {data['temp'].max()}")
# print(f"Min Temperature is: {data['temp'].min()}")

# Get data in columns
# print(data['condition'])
# OR
# print(data.condition)

# Get a row of data
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# # print(monday.condition)
# # FORMULA: YOUR_TEMP * 1.8 + 32 |------------------------------------------------
# print(monday.temp * 1.8 + 32)

# Create a dataframe from scratch
data_dict = {
    'student': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')  # creating a new csv file and adding the new data to the file!
