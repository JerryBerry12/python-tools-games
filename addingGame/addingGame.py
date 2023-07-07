#Adding Game
#Never gonna give u up
# #rickroll
import os
import random
#set up functions for read file, write file, and checking if file exists
def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists

def writeFile(filePath, textToWrite):
    fileHandle = open(filePath, 'w')
    fileHandle.write(textToWrite)
    fileHandle.close()

def readFile(filePath):
    if not fileExists(filePath):
        print('The file, ' + filePath + ' does not exist - cannot read it.')
        return ''
    fileHandle = open(filePath, 'r')
    data = fileHandle.read()
    fileHandle.close()
    return data
#variable define
DATA_FILE_PATH = 'AddingGameData.txt'

if not fileExists(DATA_FILE_PATH):
    userName = input('You must be new here, please enter your name. > ')
    score = 0
    nProblems = 0
    nCorrect = 0
    
    print('To quit the game, press RETURN/ENTER and your info will be saved.')
    print('OK', userName, "let's get started...")
    print()
else:
    savedDataString = readFile(DATA_FILE_PATH)
    savedDataList = savedDataString.split(',')
    userName = savedDataList[0]
    score = savedDataList[1]
    score = int(score)
    nProblems = savedDataList[2]
    nProblems = int(nProblems)
    nCorrect = int(savedDataList[3])
    
    print('Welcome back', userName, ', nice to see you again!')
    print('Your current score is: ', score)
    print()

#Main loop

while True:
    firstNumber = random.randrange(0,11)
    secondNumber = random.randrange(0,11)
    correctAnswer = firstNumber + secondNumber

    question = 'What is: ' + str(firstNumber) + ' + ' + str(secondNumber) + '? > '
    userAnswer = input(question)
    if userAnswer == '':
        break
    userAnswer = int(userAnswer)
    nProblems = nProblems + 1

    if userAnswer == correctAnswer:
        print('Yes, you got it!')
        score = score + 2
        nCorrect = nCorrect + 1
    else:
        print('No, sorry, the correct answer was: ', correctAnswer)
        score = score - 1

    print('Your current score is: ', score)
    print()

print('Thanks for playing')
print()
print('You have tried', nProblems, 'problems and you have correctly answered', nCorrect)
#writing time!
dataList = [userName, str(score), str(nProblems), str(nCorrect)]
outputText = ','.join(dataList)

writeFile(DATA_FILE_PATH, outputText)


    