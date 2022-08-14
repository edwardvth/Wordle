import random

lines = open("5_letter_words.txt", "r").read().splitlines()
word = random.choice(lines)
word = word.upper()


board = {
    6 : ["_", "_", "_", "_", "_"],
    5 : ["_", "_", "_", "_", "_"],
    4 : ["_", "_", "_", "_", "_"],
    3 : ["_", "_", "_", "_", "_"],
    2 : ["_", "_", "_", "_", "_"],
    1 : ["_", "_", "_", "_", "_"]
}

colorList = {
    6 : [39, 39, 39, 39, 39],
    5 : [39, 39, 39, 39, 39],
    4 : [39, 39, 39, 39, 39],
    3 : [39, 39, 39, 39, 39],
    2 : [39, 39, 39, 39, 39],
    1 : [39, 39, 39, 39, 39] 
}

def boardprint():
    global board, colorList

    final = []
    for x in range(len(board)):
        spots = [f"\033[{col}m{board[x+1][idx]}\33[0m" for idx, col in enumerate(colorList[x+1])]
        l = ' '.join(spots)
        final.append(f"| {l} |")
    print('\n'.join(final))
    

    return colorList



guess = ""
result = {}

def checkRight(guess, word, row):
    global board, colorList

    GuessCheckDouble = {i:guess.count(i) for i in guess}
    WordCheckDouble = {i:word.count(i) for i in word}
    result = {key: GuessCheckDouble[key] - WordCheckDouble.get(key, 0) for key in GuessCheckDouble.keys()}
    updateRow = []
    colorRow = []

    for x in range(len(word)):
        if guess[x].upper() == word[x]: # green
            
            letter = guess[x]
            updateRow.append(letter)
            colorRow.append(32)

        elif guess[x].upper() in word and result[guess[x]] == 0: # yellow
            
            letter = guess[x]
            updateRow.append(letter)
            colorRow.append(33)
            
        else: # grey

            letter = guess[x]
            updateRow.append(letter)
            colorRow.append(30)

    

    board.update({row : [updateRow[0], updateRow[1], updateRow[2], updateRow[3], updateRow[4]]})
    colorList.update({row : [colorRow[0], colorRow[1], colorRow[2], colorRow[3], colorRow[4]]})

    winRow = [32, 32, 32, 32, 32]
    if colorRow == winRow:
        boardprint()
        print("YOU WON!")
        exit()



    return board

word = word.upper()
word = list(word)


print("hello! welcome to \033[32;1mWORDLE\033[0m")
print("\tTry to guess a 5-letter word in 6 guesses or less.\n\t\tIf a letter is \033[32mgreen\033[0m, then it is in the right place,\n\t\tIf a letter is \033[33myellow\033[0m, then it is in the wrong place, \n\t\tif a letter is \033[30mgrey\033[0m, then it is the wrong letter. \nREMEMBER\n\t - \033[1mNO\033[0m proper nouns, \n\t - \033[1mNO\033[0m punctuation, hyphens, or accent marks.")
print()
boardprint()
print()

numList = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH"]
z = 0
while z < 6:
        print()
        guess = input(f"{numList[z]} GUESS  > ")
        guess = guess.upper()
        guessL = guess.lower()
        guess = list(guess)
        if len(guess) == 5 and guessL in lines:
            checkRight(guess, word, z+1)
            boardprint()
            z += 1
        else:
            print("Please enter a valid word.")
            print()
            boardprint()
        
        if z == 6:
            wordStr = "".join(("".join(item) for item in word))
            print("\tYou \033[1mLOST\033[0m lol! The word was", wordStr.lower(), "... (Loser)")
            exit()







