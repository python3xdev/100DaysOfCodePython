# Create the logging_decorator() function 👇

def logging_decorator(func):
    def wrapper(*args):
        print(f"Function Name: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Function Output: {func(args[0], args[1])}")
    return wrapper

# Use the decorator 👇


@logging_decorator
def add_two_nums(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"


add_two_nums(5, 4)
