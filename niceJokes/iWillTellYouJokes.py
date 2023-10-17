import random
jokelist = []
file1 = open('jokefile.txt', 'r')
for line in file1:
  jokelist.append(line)
while True:
  print(random.choice(jokelist))
  userchoice = input('Another one? (y/n)')
  userchoice.lower()
  if userchoice == 'n':
    exit()
