# Multiple Choice Trivia
# never gonna


from pytrivia import Category, Diffculty, Type, Trivia
my_api = Trivia(True)
print('Welcome!')
print('To play my multiple choice trivia game, you have to enter your guess in the blank.')
while True:
    response = my_api.request(1)
    inner_dict = response['results'][0]
    list_of_answers = [inner_dict['incorrect_answers']]
    print('Question:')
    print(inner_dict['question'])
    print()
    print('Options:')
    print('a: ' + inner_dict['incorrect_answers'])
    answer = input('Your Answer (Case Sensitive): ')
    if answer == inner_dict['correct_answer']:
        print('You got it!')
    else:
        print('No, sorry. The correct answer was ' + inner_dict['correct_answer'])
    user_option = input('\n Press enter/return for another question. Press q + enter/return to exit.')
    if user_option == 'q':
        break

print('Thanks for playing!')