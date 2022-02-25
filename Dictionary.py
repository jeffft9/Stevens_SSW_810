import random

# Return a random word of length 5 from given words file


def getRandomWord():
    f = open("words.txt", "r")
    new_file = open("new_words.txt", "w")
    myWordList = []
    for x in f:
        if(len(x) == 6):  # words contain '\n' at the end which counts as 1 character, hence 6
            myWordList.append(x[:-1].upper())
            # writing to new file "new_file.txt"
            new_file.write(f"{x.upper()}")

    word = random.choices(myWordList)
    for item in word:
        finalWord = item

    f.close()
    new_file.close()
    return finalWord.upper(), myWordList
