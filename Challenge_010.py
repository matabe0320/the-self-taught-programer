#http://tinyurl.com/h9q2cpc

import random

#----------------
#function
#----------------

def hungman(word):
    wrong = 0
    stages = ["",
              "---------        ",
              "|                ",
              "|       |        ",
              "|       O        ",
              "|      /|        ",
              "|      / |       ",
              "|                "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to HANGMAN!!")
    
    while wrong < len(stages) - 1:
        print("\n")
        char = input("input one character: ")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You WIN!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You LOSE! The answer is {}".format(word))

#---------------
#main
#---------------
words_list = ["copin", "japan", "lupin", "coopo"]
index = random.randint(0, len(words_list)-1)
print("Words are...")
print(words_list)
print("\n")
hungman(words_list[index])
