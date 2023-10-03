import random

jokelist = []
jokefile = open("jokefile.txt", "r")
for line in jokefile.readlines():
  jokelist.append(line)
while True:
  print(random.choice(jokelist))
  userchoice = input('Another one? (y/n)')
  userchoice.lower()
  if userchoice == 'n':
    exit()
  