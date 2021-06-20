# DEFAULT VALUES

# def test(a='1', b='2'):
#     return f'{a} and {b}'
#
# print(test())
# print(test(b=4))

# UNLIMITED ARGUMENTS

# def add(*args):
#     return sum([n for n in args])
#
# print(add(1, 5, 8, 6))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


# print(calculate(2, add=3, multiply=5))


class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')


my_car = Car(make='Nissa', model='Skyline', color='black', seats='4')  # all of these arguments are optional
print(my_car.model)
print(my_car.make)
print(my_car.color)
print(my_car.seats)
