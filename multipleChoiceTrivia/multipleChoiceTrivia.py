# Multiple Choice Trivia
# never gonna

from pytrivia import Category, Diffculty, Type, Trivia
import random

my_api = Trivia(True)
print('Welcome!')
print(
  'To play my multiple choice trivia game, you have to enter your guess in the blank.'
)
while True:
  response = []
  inner_dict = []
  list_of_answers = []
  response = my_api.request(1)
  inner_dict = response['results'][0]
  list_of_answers = [
    inner_dict['incorrect_answers'][0], inner_dict['incorrect_answers'][1],
    inner_dict['incorrect_answers'][2], inner_dict['correct_answer']
  ]
  random.shuffle(list_of_answers)
  print('Question:')
  print(inner_dict['question'])
  print()
  print('Options:')
  print('a: ' + list_of_answers[0])
  print('b: ' + list_of_answers[1])
  print('c: ' + list_of_answers[2])
  print('d: ' + list_of_answers[3])
  option_a = list_of_answers[0]
  option_b = list_of_answers[1]
  option_c = list_of_answers[2]
  option_d = list_of_answers[3]
  answer = input('Your Answer (Case Sensitive): ')
  if option_a == inner_dict['correct_answer']:
    letter_of_correct_answer = option_a
  elif option_b == inner_dict['correct_answer']:
    letter_of_correct_answer = option_b
  elif option_c == inner_dict['correct_answer']:
    letter_of_correct_answer = option_c
  elif option_d == inner_dict['correct_answer']:
    letter_of_correct_answer = option_d
  if answer == letter_of_correct_answer:
    print('Horray! You got it right!')
  else:
    print("Sorry, you're incorrect. The correct answer is: " +
          inner_dict['correct_answer'])
  user_option = input(
    '\n Press enter/return for another question. Press q + enter/return to exit.'
  )
  if user_option == 'q':
    break

print('Thanks for playing!')
