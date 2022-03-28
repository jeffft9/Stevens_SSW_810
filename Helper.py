
def main():

    playMore = True
    while playMore:
        goodWords = input("Enter all good letters : ").upper()
        goodWords = list(goodWords.strip())
        badWords = input("Enter all bad letters : ").upper()
        badWords = list(badWords.strip())
        positionWords = input(
            "Enter characters in position, leave space where unknown : ").upper()

        try:
            fs = open("wordRank.csv", "r")
            next(fs)

            wordlist = []
            tentative = []

            for x in fs:
                wordlist.append(x[0:5])

            if len(goodWords) == 0 and len(badWords) == 0:
                print(wordlist[:50])
                break

            for x in wordlist:
                # good = all(letter in x for letter in goodWords)
                goodflag = True
                badFlag = True
                for y in goodWords:
                    if y not in x:
                        goodflag = False
                        break
                for z in badWords:
                    if z in x:
                        badFlag = False

                if goodflag and badFlag:
                    tentative.append(x)

            copyTentative = tentative[:]

            if(len(positionWords) == 5):
                for x in tentative:
                    for index in range(5):
                        if positionWords[index] != " " and positionWords[index] != x[index]:
                            copyTentative.remove(x)
                            break

            print(copyTentative)
            fs.close()
        except IOError:
            print('An error occured trying to read the file.')
            print(
                'Please make sure "wordRank.csv" is present in the directory before running the program')
            quit()

        userInput = input("Do you want to add more? : Y/N ")

        if not userInput:
            print("Invalid Input, Quitting....")
            break
        elif userInput in "yY":
            playMore = True
        elif userInput in "nN":
            playMore = False
        else:
            print("Invalid Input, Quitting....")
            break


main()
