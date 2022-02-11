# ************************************************************* PSEUDO-CODE *********************************************************
""" 
Wordle game Pseudo-code

while attempt < 6

    input(input_word)

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
            add to guessed_chars list   
    
    for i in input_word
        if i present in input_word and not present in guessed_chars
            print i is present but in wrong position
        
        else if i not present in todays_word
            add to wrong_chars
    
    print wrong_chars in sorted manner
    add input_word to entered_words
    attempt+=1

    if attempt == 6
        print unsuccessful and correct answer
        terminate the program
    
"""
# ********************************************************** SOURCE-CODE *******************************************************************

todays_word = "SONAR"

entered_words = []
guessed_chars = []
wrong_chars = []

attempt = 0

while attempt < 6:
    input_word = input(
        f'\nAttempt {attempt+1} - Please enter a 5 character word : ').upper()

    # check if entered word is having any special characters
    if input_word.isalpha() == False:
        print('\nPlease enter a word containing only Alphabets.')
        continue

    # check if entered word has already been entered before
    if input_word in entered_words:
        print(f'\n{input_word} already entered once!!!')
        continue

    # check if entered word is of length 5
    if len(input_word) != 5:
        print('WARNING : Word should be of length 5\n')
        continue

    # check if the guess is correct
    if input_word == todays_word:
        print(" Congrats! You have correctly guessed today's word!",
              '\n Thank you for Playing!!')
        break

    # comparing the characters of input_word and todays_word in corresponding position
    for index in range(len(input_word)):
        if input_word[index] == todays_word[index]:
            print(
                f'\n{input_word[index]} is in the Right Position, Keep going!')
            guessed_chars.append(input_word[index])

    # checking which characters of input_word are present and absent in todays_word
    for character in input_word:
        if todays_word.find(character) >= 0 and character not in guessed_chars:
            print(
                f"\n{character} is present in today's word, but not in the position you mentioned")
        elif todays_word.find(character) == -1:
            wrong_chars.append(character)

    wrong_chars.sort()

    print(f"\nCharacters not Present in today's word : {wrong_chars}")
    entered_words.append(input_word)
    attempt += 1

    if attempt == 6:
        print("\nUnfortunately, you were unable to guess today's word")
        print(f"Today's word was {todays_word}")
