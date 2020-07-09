import hangman_stages
import wordList
import random


guessed_letters = []
def add_letter(letter):
    letter = letter.upper()
    if (letter not in guessed_letters):
        guessed_letters.append(letter)
def show_letters_list():
    str_of_letters = "["
    for i in range(len(guessed_letters)):
        str_of_letters += guessed_letters[i]
        if i != len(guessed_letters)-1:
            str_of_letters += " "
    str_of_letters += "]"
    str_of_letters = str_of_letters.upper()
    return str_of_letters
def errorChecker(errors):
    if (errors == 0):
        print(hangman_stages.initial_hangman)
    elif (errors == 1):
        print(hangman_stages.one_wrong_hangman)
    elif (errors == 2):
        print(hangman_stages.two_wrong_hangman)
    elif (errors == 3):
        print(hangman_stages.three_wrong_hangman)
    elif (errors == 4):
        print(hangman_stages.four_wrong_hangman)
    elif (errors ==5):
        print(hangman_stages.five_wrong_hangman)
    elif (errors == 6):
        print(hangman_stages.six_wrong_hangman)
def hangman ():
    global guessed_letters
    guess_letters = []
    key = wordList.list[random.randrange(len(wordList.list)-1)]
    final_key = key
    key = key.upper()
    hint = ""
    errors = 0
    for i in key:
        hint+= "_"
    while(key!=len(key)*"_"):
        if errors==6:
            print("You lose!")
            break
        errorChecker(errors)
        print(hint)
        print(show_letters_list())
        guess = (input("Guess: ")).upper()
        if guess in key:
            while(key.find(guess)!=-1):
                if key.find(guess)==0:
                    hint = guess + hint[1:len(key)]
                    key = "_" + key[1:len(key)]
                elif key.find(guess) == len(key)-1:
                    hint = hint[0:len(key)-1] + guess
                    key = key[0:len(key)-1] + "_"
                else:
                    hint = hint[0: key.find(guess)] + guess + hint[key.find(guess) +1 : len(key)]
                    key = key[0: key.find(guess)] + "_" + key[key.find(guess) +1 : len(key)]
        elif guess in guessed_letters:
            print("You already guess that!")
        else:
            add_letter(guess)
            print("Incorrect")
            errors+=1
    print("You finished with " + str(errors) + " error(s).")
    print("The word was " + final_key + ".")
hangman()