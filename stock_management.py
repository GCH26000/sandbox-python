class User:
    def __init__(self, name, function):
        self.name = name
        self.function = int(function)

class Thing:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

def stock_management():
    actualUser = intro()
    print("Hello "+ actualUser.name + ", what do you want to do ?");
    



def intro():
    print("please enter your name :")
    name = input()
    print("Are you \n 1-- A customer \n 2-- A supplier")
    function = input()
    return User(name, function)

def menus(function): 
    if function == 1 :
        print("1-- Buy things")
    elif function == 2:
        print("1-- Add stock \n 2-- Add material")