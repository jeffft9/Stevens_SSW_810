# Get input from user
def inputFromUser(attempt):
    input_word = input(
        f'\nAttempt {attempt+1} - Please enter a 5 character word : ').upper()
    return input_word

# check if entered word is having any special characters


def checkInput(input_word):
    if input_word.isalpha() == False:
        print('\nWARNING : Please enter a word containing only Alphabets.')
        return False
    else:
        return True

# check if entered word has already been entered before


def checkWordUsed(input_word, entered_words):
    if input_word in entered_words:
        print(f'\nWARNING : {input_word} already entered once!!!')
        return False
    else:
        return True


# check if entered word is of length 5
def checkWordLength(input_word):
    if len(input_word.strip()) != 5:
        print('\nWARNING : Word should be of length 5')
        return False
    else:
        return True
