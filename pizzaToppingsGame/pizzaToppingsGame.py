# Pizza Toppings Game
# Never gonna give u up

import time

def showPizzaToppings(theList):
    print()
    if len(theList) == 0:
        print('Your pizza has no toppings.')
    else:
        print('The toppings on your pizza are: ')
        print()
        for thisItem in theList:
            print('      ' + thisItem)
    print()

#main code
print('Welcome to my pizzeria, where you get to choose your toppings.')
print('When prompted, enter the first letter or the full word of what you want to do.')
print()
print('---- Operations ----')
print('a/add\t\t\tAdd a topping')
print('c/change\t\t\tChange a topping')
print('o/order\t\t\tOrder the pizza')
print('q/quit\t\t\tQuit')
print('r/remove\t\t\tRemove a topping')
print('s/startover\t\t\tStart over')
print()

toppingsList = [ ]
while True:

    print('What would you like to do?')
    menuChoice = input('add, change, order, quit, remove, startover > ')

    if (menuChoice == 'a') or (menuChoice == 'add'): #add a topping
        newTopping = input('Type in a topping to add. > ')
        toppingsList.append(newTopping)

    elif (menuChoice == 'c') or (menuChoice == 'change'): #change a topping
        oldTopping = input('What topping would you like to change? > ')
        if oldTopping in toppingsList:
            index = toppingsList.index(oldTopping)
            newTopping = input('What is the new topping? > ')
            toppingsList[index] = newTopping
        else:
            print(oldTopping, ' was not found.')
    elif (menuChoice == 'o') or (menuChoice == 'order'): #order the current pizza
        showPizzaToppings(toppingsList)
        print("here's your pizza!")
        print()
        time.sleep(2)
        print('Ordering now!')
        time.sleep(1)
        print('Give me a moment...')
        time.sleep(5)
        print('Done! Thanks for your order!')
        print()
        time.sleep(2)
        another = input('Would you like to order another pizza? (y/n)? > ')
        if another == 'y':
            toppingsList = [ ]
        else:
            break
    
    elif (menuChoice == 'q') or (menuChoice == 'quit'): #quit
        break

    elif (menuChoice == 'r') or (menuChoice == 'remove'): #remove a topping
        delTopping = input('What topping would you like to remove? > ')
        if delTopping in toppingsList: 
            index = toppingsList.index(delTopping)
            toppingsList.pop(index)
        else:
            print(delTopping, ' was not found.')
    
    elif (menuChoice == 's') or (menuChoice == 'startover'): #reset pizza
        print("OK, let's start over.")
        toppingsList = [ ]
    else:
        print("Uh... Sorry, I'm not sure what you said, please try again.")
    
    showPizzaToppings(toppingsList)

print()
print('Thanks for coming to my pizzeria! Please come agian!')
