# ansh bhai 

def chota_deco(func):
    def wrapper(x):
        print("Hello" , x)
    return wrapper

@chota_deco
def more_chota_deco(name):
    print(name)

more_chota_deco("chotu")


def print_args_decorator(func):
    def wrapper(*args, **kwargs):
        print(f" Positional arguments (*args): {args}")
        print(f" Keyword arguments (**kwargs): {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@print_args_decorator
def greet(age, name, city):
    print(f"Hello, {name}! You are {age} years old from {city}.")

greet(18,city="yelle",name="Ansh")
