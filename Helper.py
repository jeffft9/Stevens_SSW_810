from platform import node
from LinkedList import Node
from LinkedList import SLinkedList


def main():

    playMore = True
    while playMore:
        goodWords = input("Enter all good letters : ").upper()
        if not all(x.isalpha() or x.isspace() for x in goodWords):
            continue

        if len(goodWords) > 5:
            print("You can have only 5 maximum good letters")
            continue

        goodWords = list(goodWords.strip())

        badWords = input("Enter all bad letters : ").upper()
        if not all(x.isalpha() or x.isspace() for x in badWords):
            continue

        badWords = list(badWords.strip())

        if any(x in goodWords for x in badWords):
            print('\nWARNING : A letter cannot be both good and bad!')
            continue

        positionWords = input(
            "Enter characters in position, leave space where unknown : ").upper()
        if len(positionWords) != 0:
            if len(positionWords) != 5:
                print('\nWARNING : Word should be of length 5 or empty')
                continue

        if not all(x.isalpha() or x.isspace() for x in positionWords):
            print('\nWARNING : Please enter a word containing only Alphabets or Spaces.')
            continue

        try:
            fs = open("wordRank.csv", "r")
            next(fs)

            wordlist = []
            tentative = []

            for x in fs:
                wordlist.append(x[0:5])

            # If user does not provide Good or bad words, then display top 50 words
            if len(goodWords) == 0 and len(badWords) == 0:
                # print(wordlist[:50])
                linkedList = SLinkedList()
                linkedList.headval = Node(wordlist[0])
                node1 = linkedList.headval

                for val in wordlist[1:50]:
                    node1.nextval = Node(val)
                    node1 = node1.nextval

                # print(copyTentative)
                print()
                linkedList.listprint()
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

            linkedList = SLinkedList()
            linkedList.headval = Node(copyTentative[0])
            node1 = linkedList.headval

            for val in copyTentative[1:]:
                node1.nextval = Node(val)
                node1 = node1.nextval

            # print(copyTentative)
            print()
            linkedList.listprint()

            fs.close()
        except IOError:
            print('An error occured trying to read the file.')
            print(
                'Please make sure "wordRank.csv" is present in the directory before running the program')
            quit()

        userInput = input("\nDo you want to try again? : Y/N ")

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


if __name__ == "__main__":
    main()
