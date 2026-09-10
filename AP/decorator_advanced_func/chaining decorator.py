def decor1(funcx):
    def wrapper():
        print("decor 1 ")
        funcx()
        print("decor 1 ended")
    return wrapper


def decor2(funcx):
    def wrapper():
        print("decor 2 ")
        funcx()
        print("decor 2 ended")
    return wrapper
    


def welcome():
    print("Welcome to the advanced python example!")

# def square():
#     x = int(input("enter value = "))
#     print (x**2)


x = decor2(decor1(welcome))

# y = decor1(square)

x()

