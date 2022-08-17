import random

allWords = open("5_letter_words.txt", "r").read().splitlines()
word = random.choice(allWords)
word = word.upper()


GREEN = 32
YELLOW = 33
GREY = 30
WHITE = 39
BOLD = 1



board = {n+1: ["_"]*5 for n in range(6)}
colorList = {n+1: [WHITE]*5 for n in range(6)}



def boardprint(board, colorList):

    final = []
    for x in range(len(board)):
        spots = []
        for idx, color in enumerate(colorList[x+1]):
            spots.append(f"\033[{color}m{board[x+1][idx]}\33[0m")
        l = ' '.join(spots)
        final.append(f"| {l} |")
    print('\n'.join(final))
    

def checkGuess(guess : str, word : str, boardRow : int, board, colorList):

    GuessCheckMulti = {i : guess.count(i) for i in guess}
    WordCheckMulti = {i : word.count(i) for i in word}
    result = {key: GuessCheckMulti[key] - WordCheckMulti.get(key, 0) for key in GuessCheckMulti.keys()}
    wordRow = []
    colorRow = []

    for x in range(len(word)):
        if guess[x].upper() == word[x]: # green
            
            letter = guess[x]
            wordRow.append(letter)
            colorRow.append(GREEN)

        elif guess[x].upper() in word and result[guess[x]] == 0: # yellow
            
            letter = guess[x]
            wordRow.append(letter)
            colorRow.append(YELLOW)
            
        else: # grey

            letter = guess[x]
            wordRow.append(letter)
            colorRow.append(GREY)

    

    board.update({boardRow : wordRow})
    colorList.update({boardRow : colorRow})

    winRow = [GREEN for i in range(5)]
    if colorRow == winRow:
        boardprint(board, colorList)
        print("YOU WON!")
        exit()



    return board


def instructions():
    print(
        f"""
        \nhello! welcome to \033[{GREEN};{BOLD}mWORDLE\033[0m
        \tTry to guess a 5-letter word in 6 guesses or less.
        \t\tIf a letter is \033[{GREEN}mgreen\033[0m, then it is in the right place,
        \t\tIf a letter is \033[{YELLOW}myellow\033[0m, then it is in the wrong place, 
        \t\tif a letter is \033[{GREY}mgrey\033[0m, then it is the wrong letter. \n
        \tREMEMBER
        \t\t - \033[{BOLD}mNO\033[0m proper nouns, 
        \t\t - \033[{BOLD}mNO\033[0m punctuation, hyphens, or accent marks.")

        """
    )

    print()
    boardprint(board, colorList)
    print()




if __name__ == "__main__":
    instructions()
    numList = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH"]
    z = 0
    while z < 6:
            print()
            guess = input(f"{numList[z]} GUESS  > ")
            guess = guess.upper()
            guessL = guess.lower()
            guess = list(guess)
            if guessL in allWords:
                checkGuess(guess, word, z+1, board, colorList)
                boardprint(board, colorList)
                z += 1
            else:
                print("Please enter a valid word.")
                print()
                boardprint(board, colorList)
            
            if z == 6:
                print(f"\tYou \033[{BOLD}mLOST\033[0m! The word was \033[{GREEN};{BOLD}m{word}\033[0m...")
                exit()
