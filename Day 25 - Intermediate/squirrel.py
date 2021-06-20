import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = 0
red = 0
black = 0

for color in data['Primary Fur Color']:
    if color == 'Gray':
        gray += 1
    elif color == 'Cinnamon':
        red += 1
    elif color == 'Black':
        black += 1

data_dict = {
    'Fur Color': ['Gray', 'Red', 'Black'],
    'Count': [gray, red, black],
}

# print(data_dict)

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
