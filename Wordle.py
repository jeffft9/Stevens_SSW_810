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

from decimal import DivisionByZero
from UI import Ui
import Dictionary as dictionaryClass
from calculateStatistics import CalculateStatistics
from typing import Dict, List, Tuple
from Helper import Helper
import Database

"""The structure of this Class is such that it does not need getters or setters since
all data is acquired from another Class in the constructor"""


class Wordle:
    def __init__(self) -> None:
        self.dictionary = dictionaryClass.Dictionary()

    def __str__(self) -> None:
        return "Main Game class"

    # Initialise all variables
    def initVariables(self, words_used: List[str]) -> Tuple[str, List, List, str, int, List, str, str]:
        todays_word, word_list = self.dictionary.getRandomWord(words_used)
        # print(str(self.dictionary))
        words_used.append(todays_word)
        entered_words = []
        answer = [None, None, None, None, None]
        attempt = 0
        good_letters = ""
        bad_letters = ""
        # print(todays_word)
        return todays_word, word_list, entered_words, answer, attempt, words_used, good_letters, bad_letters

    def main(self):

        words_used = []
        todays_word, word_list, entered_words, answer, attempt, words_used, good_letters, bad_letters = self.initVariables(
            words_used)
        games_played = 0
        games_won = 0
        guess_history = []

        while attempt < 6:
            if games_played == 1000:
                break
            # input_word = Ui.inputFromUser(attempt)
            new_answer = ""
            if all(v is not None for v in answer):
                for char in answer:
                    if char == "`" or char == '"':
                        new_answer += " "
                    else:
                        new_answer += char
            input_word = Helper.help(
                good_letters, bad_letters, new_answer, entered_words)

            # print(f"Word chosen for attempt - {attempt+1} : {input_word}")

            # if empty word entered then quit playing
            if(len(input_word.strip()) == 0):
                print("\nThank you for Playing.!")
                print("\nExiting")
                self.displayResults(games_played, games_won, guess_history)
                break

            # check if entered word is having any special characters
            if(not Ui.checkInput(input_word)):
                continue

            # check if entered word has already been entered before
            if(not Ui.checkWordUsed(input_word, entered_words)):
                continue

            # check if entered word is of length 5
            if(not Ui.checkWordLength(input_word)):
                continue

            # check if word was entered previously
            if(input_word not in word_list):
                print("\nWARNING : Entered word not in dictionary!")
                continue

            # check if the guess is correct
            if input_word == todays_word:
                print(" \nCongrats! You have correctly guessed today's word!",
                      '\n Thank you for Playing!!')
                print(f" The word was {todays_word}")
                games_played += 1
                games_won += 1
                guess_history.append(attempt+1)
                self.displayResults(games_played, games_won, guess_history)
                Database.everyGameDb(
                    games_played, todays_word, attempt, "Successful", " ".join(entered_words))
                todays_word, word_list, entered_words, answer, attempt, words_used, good_letters, bad_letters = self.initVariables(
                    words_used)
                # print("Starting a New Game, Press enter to exit")
                continue
                # break

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
                    if input_word[index] not in good_letters:
                        good_letters += input_word[index]
                else:
                    answer[index] = '"'

            # checking which characters of input_word are present and absent in todays_word
            for index in range(len(input_word)):
                if input_word[index] != todays_word[index]:
                    if input_word[index] in letter_counts:
                        if letter_counts[input_word[index]] > 0:
                            letter_counts[input_word[index]] -= 1
                            answer[index] = "`"
                            if input_word[index] not in good_letters:
                                good_letters += input_word[index]
                    else:
                        if input_word[index] not in bad_letters:
                            bad_letters += input_word[index]

            entered_words.append(input_word)
            attempt += 1

            # print(f"The good letters for chosen word : " + good_letters)
            # print(f"The bad letters for chosen word : " + bad_letters)

            if attempt == 6:
                print("\nUnfortunately, you were unable to guess today's word")
                print(f"Today's word was {todays_word}")
                games_played += 1
                guess_history.append("Unsuccessful")
                self.displayResults(games_played, games_won, guess_history)
                Database.everyGameDb(
                    games_played, todays_word, -1, "Unsuccessful", " ".join(entered_words))
                todays_word, word_list, entered_words, answer, attempt, words_used, good_letters, bad_letters = self.initVariables(
                    words_used)

                # print("Starting a New Game, Press enter to exit")
                # break
                continue

    def displayResults(self, games_played: int, games_won: int, guess_history: List[str]) -> None:
        print(f"\nNumber of Games Played : {games_played}")
        # print(f"Guess distribution : {guess_history}")

        # try:
        #     print(f"Win % : {(games_won/games_played)*100}")
        # except ZeroDivisionError:
        #     print('Win % : 0')

        # try:
        #     f = open("gameplay.log", "a")
        #     f.write((f"Number of Games Played : {games_played}\n"))
        #     f.write(f"Guess distribution : {guess_history}\n")
        #     f.write(f"Win % : {(games_won/games_played)*100}\n\n")
        #     f.close()
        # except IOError:
        #     print('An error occured trying to read the file.')
        #     print(
        #         'Please make sure "gameplay.log" is present in the directory before running the program')
        #     quit()
        # except ZeroDivisionError:
        #     f.write(f"Win % : 0\n\n")


if __name__ == "__main__":
    Database.truncateWordle()
    game = Wordle()
    game.main()
    print()
    print("**********************************************DATABASE CONTENT**********************************************")
    Database.queryWordle()
    Database.calcStats()
    stats = CalculateStatistics()
    stats.calculateAndSortWords()
