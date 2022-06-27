from generator import generatePassword, hello_world
from stock_management import stock_management

def choices(choice):
    if choice == 1 :
        hello_world()
    elif choice == 2 :
        print("Please select the length of the password :")
        len = input()
        password = generatePassword(int(len))
        print("Your generated password is : " +password)
    elif choice == 3 :
        stock_management()