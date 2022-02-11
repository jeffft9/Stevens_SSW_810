import random

# Return a random word of length 5 from given words file


def getRandomWord():
    f = open("words.txt", "r")
    myWordList = []
    for x in f:
        if(len(x) == 6):  # words contain '\n' at the end which counts as 1 character, hence 6
            myWordList.append(x[:-1].upper())

    word = random.choices(myWordList)
    for item in word:
        finalWord = item

    return finalWord.upper(), myWordList
