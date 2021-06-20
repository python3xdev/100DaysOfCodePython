# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# Error Handling

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message: # saving the original error as a variable...
#     print(f"The key {error_message} does not exist.")
# else:
#     data = file.read()
#     print(data)
# finally:
#     file.close()
#     print("File was closed.")

height = float(input("Height in meters: "))
weight = int(input("Weight in kilos: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

