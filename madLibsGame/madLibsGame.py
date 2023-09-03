# Mad Libs
# Rick Roll goes here
# Dun Dun Dun Dun Dun Dun

while True:
  boyname = input('Masucline Name: ')
  occupation = input('Occupation: ')
  foreign_country = input('Foreign Country: ')
  adjective1 = input('Adjective: ')
  verb1 = input('Past Tense Verb: ')
  adjective2 = input('Adjective: ')
  verb2 = input('Verb: ')
  number1 = input('Number: ')
  noun1 = input('Noun: ')
  verb3 = input('Verb: ')
  noun2 = input('Noun: ')
  number2 = input('Number: ')
  p_noun1 = input('Plural Noun: ')
  verb4 = input('Verb: ')
  p_noun2 = input('Plural Noun: ')
  verb5 = input('Verb: ')
  noun3 = input('Noun: ')
  noun4 = input('Noun: ')
  p_noun3 = input('Plural Noun: ')
  verb6 = input('Verb: ')
  noun5 = input('Noun: ')
  verb7 = input('Verb: ')
  p_noun4 = input('Plural Noun: ')
  verb8 = input('Verb: ')
  number3 = input('Number: ')
  lengthOfTime = input('Length of time, Example: 12 days, 12 weeks etc: ')

  print()
  print("My little brother, " + boyname + ", is the " + occupation + " of " +
        foreign_country + "!")
  print("He has shown " + adjective1 + " promise since he was " + verb1 + ".")
  print("He is so " + adjective2 + " that he tried to " + verb2 + " once!")
  print("It took him " + number1 + " days to get himself out of that " +
        noun1 + "!")
  print("By last year, he was determined to " + verb3 + " for " + occupation +
        ".")
  print("He sure had his work cut out for him!")
  print("First, little " + boyname + " had to enter his " + noun2 +
        " next to the " + number2 + " other " + p_noun1)
  print("Then he had to " + verb4 + p_noun2 + ", " + verb5 + " the " + noun3 +
        ", and bribe potential voters with " + noun4 + ".")
  print("Finally, the day came when " + p_noun3 + " came from all over " +
        foreign_country + " to " + verb6 + ".")
  print('I held a ' + noun5 + ' saying, "' + verb7 + ' for ' + boyname + '! ' +
        p_noun4 + ' for everyone!"')
  print("By the end of the day, it was clear that " + boyname + " had " +
        verb8 + ".")
  print(
    "His important job supports the entire family with a sound income of " +
    number3 + " thousand dollars per " + lengthOfTime + ".")
  print()

  answer = input('Type "q" to quit, or anything else to continue: ')
  if answer == 'q':
    break

print('Bye')
