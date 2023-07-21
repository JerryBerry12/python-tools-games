import wikipedia

while True:
    newstring = input('>')
    if newstring == 'exit':
        print('Bye!')
        exit()
    try:
        result = wikipedia.summary(newstring, auto_suggest=False, sentences=2)
        print(result)
    except:
        print("We couldn't find what you searched for, please try again.")
    

