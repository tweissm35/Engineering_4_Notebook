from findAll import findAll
from stickMan import stickMan

word = input("Pick a word: ").lower()  #get word and force lowercase

guess = []  #list for tracking guessed letters
places = []  #list for tracking correctly guessed places
wrongs = 0

if not word.isalpha():
    PUNCTUATION = ' -_/`~.:[]{}|=+-_,;\'"!@#$%^&*()?12345677890'
    for p in PUNCTUATION:
        places += findAll(word, p)  # reveals funny stuff and spaces

print('\n' * 40)

while True:
    letter = input(
        "Guess a letter: ").lower()  #Get input letter and force lowercase
    if len(letter) != 1:  #Makes sure there is exactly one letter
        print("You must enter one letter")
    else:
        if letter not in guess:  #checks if letter already guessed
            guess.append(letter)  #add letter to list of guessed
            if letter in word:  #check if
                print("Yes! There is " + str(word.count(letter)))
                places += findAll(word, letter)
            else:
                print("wrong")
                wrongs += 1
        else:
            print("You already guessed that letter")

    for i in range(len(word)):  #Loops through word to display numbers
        if i in places:  #checks if the current number is guessed
            print(word[i], end=' ')
        else:
            print("_ ", end='')

    print('\n')
    stickMan(wrongs)  #print appropriate stickman

    if (len(places) == len(word)):  #check if all letters correctly guessed
        print("Congratulations, you did it")
        break
    if (wrongs >= 6):  #check if dead
        print("Too many wrong guesses")
        break
