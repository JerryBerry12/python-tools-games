# Mad Libs
# Rick Roll goes here
# Dun Dun Dun Dun Dun Dun 

while True:
    noun = input('Enter a noun: ')
    verb = input('Enter a verb: ')
    adjective = input('Enter an adjective: ')
    noun2 = input('Enter a noun: ')
    noun3 = input('Enter another noun: ')
    
    sentence = noun + ' ' + verb + ' through the ' + noun2 + ', hoping to escape the ' + adjective + ' ' + noun3 + '.'
    print()
    print(sentence)
    print()

    answer = input('Type "q" to quit, or anything else to continue: ')
    if answer == 'q':
        break

print('Bye')