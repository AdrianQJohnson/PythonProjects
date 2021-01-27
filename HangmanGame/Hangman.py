import json

word = "hangman"
hidden = ""
incorrectCount = 0
maxTries = 6

def init():
    with open('HangmanJSON/words.json') as f:
        data = json.load(f)
    print(data)
    for x in range(len(word)):
        global hidden
        hidden = hidden + "_"

def incorrect():
    global incorrectCount
    incorrectCount = incorrectCount + 1
    if incorrectCount == maxTries:
        print("Game Over")
        quit(0)
    else:
        print("Remaining Attempts:", maxTries - incorrectCount)

def guess(letter):
    flag = 0
    for x in range(len(word)):
        global hidden
        if word[x] == letter:
            temp = ""
            for y in range(x):
                temp = temp + hidden[y]
            temp = temp + letter
            for y in range(x + 1, len(word)):
                temp = temp + hidden[y]
            hidden = temp
            flag = 1
    if flag == 0:
        print(letter, "is not in the word")
        incorrect()
    else:
        print(letter, "is in the Word!")

def checkWin():
    flag = 0
    for x in range(len(word)):
        if hidden[x] == '_':
            flag = 1
    if flag == 0:
        print("You Won! The word was:", word)
        exit(0)

init()
while True:
    letter = input("Guess a Letter: ")
    guess(letter)
    checkWin()
    print(hidden)
    print()