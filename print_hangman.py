def print_hangman(lifes_left):
    if lifes_left == 9:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("Lifes left: ", lifes_left)
    elif lifes_left == 8:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("____")
        print("Lifes left: ", lifes_left)
    elif lifes_left == 7:
        print(" ")
        print(" ")
        print(" ")
        print(" | ")
        print(" | ")
        print("____")
        print("Lifes left: ", lifes_left)
    elif lifes_left == 6:
        print(" ")
        print("  ")
        print("  ")
        print(" | ")
        print(" | ")
        print("____")
        print("Lifes left: ", lifes_left)
    elif lifes_left == 5:
        print(" _________")
        print(" | ")
        print(" | ")
        print(" | ")
        print(" | ")
        print("____")
        print("Lifes left: ", lifes_left)
    elif lifes_left == 4:
        print(" _________")
        print(" |       |")
        print(" | ")
        print(" | ")
        print(" | ")
        print("____")
        print("Lifes left: ", lifes_left)
    elif lifes_left == 4:
        print(" _________")
        print(" |       |")
        print(" |       O")
        print(" | ")
        print(" | ")
        print("____")
        print("Lifes left: ", lifes_left)
    elif lifes_left == 3:
        print(" _________")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" | ")
        print("____")
        print("Lifes left: ", lifes_left)
    elif lifes_left == 2:
        print(" _________")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" | ")
        print("____")
        print("Lifes left: ", lifes_left)
    elif lifes_left == 1:
        print(" _________")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |      / ")
        print("____")
        print("Lifes left: ", lifes_left)
    else:
        print(" _________")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |      / \\")
        print("____")
        print("********************\n--== GAME OVER ==--\n********************")