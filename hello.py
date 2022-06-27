from menu import choices

intro = "Welcome to my world ! Please select your activity :\n 1-- Hello world \n 2-- Password Generator \n 3-- Stocks management"
print(intro)
choice = input()

choices(int(choice))
