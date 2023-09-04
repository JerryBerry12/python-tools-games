print("Welcome to knock-knock jokes.")
print("Here you will share knock-knock jokes with me.")
print('To exit, enter the keyword "exit" when I ask you who is there.')
print("Well, what are you waiting for? Let's begin!")
while True:
  print("Knock-knock")
  answer1 = input("Who's there?")
  if answer1 == "exit":
    print('thanks for playing!')
    exit()
  answer2 = input("Well then, " + answer1 + " who?")
  print("Ha-ha-ha")
