def add(*args):
    '''*args can take "n" number of arguments
    we can call *number, *anyname like variable - default *args'''
    print(args[1])
    # the type of *args is "Tuple"
    return sum(args)


v = add(1,2,3,4,5,5)
print(v)

def calculate(n,**kwargs):
    '''**kwargs - keyword arguments while call the function
    this type is dictionary. same like above we can give any name **name, **anything'''
    print(type(kwargs))
    # it will print as dictionary
    print(kwargs)
    print(kwargs["name"])
    n += kwargs["add"]
    n *= kwargs["anything"]
    print(n)

calculate(2, add=1, anything= 45, name="uday")


# we can create class with **kwargs

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.price = kw.get("price")

car = Car(make="honda", model="city")
print(car.model)
# price argument we are not passed while initialize the object
# we using "get"method to not show an error instead it will return "none"
print(car.price)