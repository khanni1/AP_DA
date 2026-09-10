def decor1(funcx):
    def wrapper():
        print("kushal's")
        funcx()
        print("THE END")
    return wrapper
    


def welcome():
    print("Welcome to the advanced python example!")

def square():
    x = int(input("enter value = "))
    print (x**2)


x = decor1(welcome)

y = decor1(square)

x()
y()

