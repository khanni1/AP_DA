def square(funx):
    def wrapper():
       x = funx()
       return(x**2)
    return wrapper

def doubles(funx):
    def wrapper():
        y  = funx()
        print(2*y)
    return wrapper

@doubles
@square
def io():
    num = int(input("Enter a Integer"))
    return num
       

