import random
from typing import List, Tuple

# Return a random word of length 5 from given words file


def getRandomWord(words_used: List[str]) -> Tuple[str, List]:
    try:
        f = open("words.txt", "r")
        new_file = open("new_words.txt", "w")
        myWordList = []
        for x in f:
            if(len(x) == 6):  # words contain '\n' at the end which counts as 1 character, hence 6
                myWordList.append(x[:-1].upper())
                # writing to new file "new_file.txt"
                new_file.write(f"{x.upper()}")

        for item in words_used:
            myWordList.remove(item)

        if len(myWordList) == 0:
            for x in f:
                if(len(x) == 6):  # words contain '\n' at the end which counts as 1 character, hence 6
                    myWordList.append(x[:-1].upper())

        word = random.choices(myWordList)
        for item in word:
            finalWord = item

        f.close()
        new_file.close()

    except IOError:
        print('An error occured trying to read the file.')
        print('Please make sure "words.txt" is present in the directory before running the program')
        quit()
    else:
        return finalWord.upper(), myWordList
