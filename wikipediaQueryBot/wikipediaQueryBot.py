import wikipediaapi
wikimod = wikipediaapi.Wikipedia('wikipediaQueryBot (https://github.com/JerryBerry12/python-tools-games/tree/master/wikipediaQueryBot)', 'en')

while True:
    newstring = input('>')
    if newstring == 'exit':
        print('Bye!')
        exit()
    itpage = wikimod.page(newstring)
    itpage.summary()
    

