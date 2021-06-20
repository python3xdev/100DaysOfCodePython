# age: int

# age = "16"

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


# print(police_check.__annotations__) # this will tell you the data types of the function

if police_check(16):
    print("You are free to go.")
else:
    print("You get a fine.")
