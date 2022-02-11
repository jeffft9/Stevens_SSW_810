# ************************************************************* PSEUDO-CODE *********************************************************
"""
Wordle game Pseudo-code

Note - Output String is displayed in form of a List for better Display and understanding 

get a random word from text file

while attempt < 6

    input(input_word)

    if length of input_word is 0
        quit playing

    if input_word is not present in dictionary 
        give warning and start again

    if input_word is having characters other than alphabets
        give warning and start again

    if input_word present in entered_words
        give warning and start again

    if length(input_word) !=5
        give warning and start again

    if input_word == todays_word
        print success and terminate program

    for index = 0 till length(input_word)
        if input_word[index] == todays_word[index]
            print input_word[index]
            reduce count in dictionary - letter_counts
        else
            mark '"' (not present)

    for i in input_word
        if i present in input_word
            if count > 0 in letter_counts
                print i is present but in wrong position
                reduce count in dictionary - letter_counts

    
    add input_word to entered_words
    attempt+=1

    if attempt == 6
        print unsuccessful and correct answer
        re-initialise the variables
        restart the program

"""
# ********************************************************** SOURCE-CODE *******************************************************************

from UI import *
from Dictionary import *


# Initialise all variables
def initVariables():
    todays_word, word_list = getRandomWord()
    entered_words = []
    answer = [None, None, None, None, None]
    attempt = 0
    # print(todays_word)
    return todays_word, word_list, entered_words, answer, attempt


def main():

    todays_word, word_list, entered_words, answer, attempt = initVariables()
    games_played = 0
    games_won = 0
    guess_history = []

    while attempt < 6:
        input_word = inputFromUser(attempt)

        # if empty word entered then quit playing
        if(len(input_word.strip()) == 0):
            print("\nThank you for Playing.!")
            print("\nExiting")
            break

        # check if entered word is having any special characters
        if(not checkInput(input_word)):
            continue

        # check if entered word has already been entered before
        if(not checkWordUsed(input_word, entered_words)):
            continue

        # check if entered word is of length 5
        if(not checkWordLength(input_word)):
            continue

        # check if word was entered previously
        if(input_word not in word_list):
            print("\nWARNING : Entered word not in dictionary!")
            continue

        # check if the guess is correct
        if input_word == todays_word:
            print(" Congrats! You have correctly guessed today's word!",
                  '\n Thank you for Playing!!')
            games_played += 1
            games_won += 1
            guess_history.append(attempt+1)
            displayResults(games_played, games_won, guess_history)
            todays_word, word_list, entered_words, answer, attempt = initVariables()
            print("Starting a New Game, Press enter to exit")
            continue

        letter_counts = {}

        # Generate a dictionary to store letter count
        for letter in todays_word:
            if letter in letter_counts.keys():
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

        # comparing the characters of input_word and todays_word in corresponding position
        for index in range(len(input_word)):
            if input_word[index] == todays_word[index]:
                answer[index] = todays_word[index]
                letter_counts[todays_word[index]] -= 1
            else:
                answer[index] = '"'

        # checking which characters of input_word are present and absent in todays_word
        for index in range(len(input_word)):
            if input_word[index] != todays_word[index]:
                if input_word[index] in letter_counts:
                    if letter_counts[input_word[index]] > 0:
                        letter_counts[input_word[index]] -= 1
                        answer[index] = "`"

        entered_words.append(input_word)
        attempt += 1
        print(answer)

        if attempt == 6:
            print("\nUnfortunately, you were unable to guess today's word")
            print(f"Today's word was {todays_word}")
            games_played += 1
            guess_history.append("Unsuccessful")
            displayResults(games_played, games_won, guess_history)
            todays_word, word_list, entered_words, answer, attempt = initVariables()
            print("Starting a New Game, Press enter to exit")


def displayResults(games_played, games_won, guess_history):
    print(f"\nNumber of Games Played : {games_played}")
    print(f"Guess distribution : {guess_history}")
    print(f"Win % : {(games_won/games_played)*100}")


if __name__ == "__main__":
    main()
