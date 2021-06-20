with open('file1.txt', mode='r') as file:
    data1 = file.readlines()

with open('file2.txt', mode='r') as file:
    data2 = file.readlines()

result = [int(num) for num in data1 if num in data2]

# Write your code above 👆

print(result)
