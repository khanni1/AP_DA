

def decor1(funcx):
    funcx.count = 0
    def wrapper():
        print("kushal's".upper())
        funcx.count += 1
        out = funcx()
        print(out.upper())
        print("THE END")
        
        print(funcx.count)
    return wrapper
    


def welcome():
    return("Welcome to the advanced python example!")

def square(x):
    return (x**2)


x = decor1(welcome)



x()
x()
x()


