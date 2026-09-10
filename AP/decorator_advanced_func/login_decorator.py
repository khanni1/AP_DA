def decor1(funx):
    def wrapper():
        print("Hello my Website")
        status =  funx()
        if(status):
            print("success in login")
        else :
            print("failed in login")
        print("Copy right kk website")
    return wrapper


@decor1
def login():
    passx = input("Enter Password: ")
    user = input("enter your: ")

    if(passx == "1234" and user.lower() == "aaa"):
        return 1
    else:
        return 0
    



login()