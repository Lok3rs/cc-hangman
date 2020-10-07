import random
import os
import sys
from print_hangman import print_hangman

words_file_path = "countries-and-capitals.txt"

def clear():
    return os.system("cls || clear")

def close():
    clear()
    return sys.exit("Thanks for playing!\n See you again!")

def random_word_from_file(file_path):
    list_of_words = []
    with open(file_path) as words:
        for line in words:
            list_of_words.append(line.replace("\n", ""))
    return random.choice(list_of_words)

def choose_difficulty(message, mininum, maximum):
    dif_lvl= 0
    while dif_lvl == 0:
        try:
            clear()
            dif_lvl = int(input("Choose your {} ( {} - {} ) \n".format(message, mininum, maximum)))
            if dif_lvl < mininum or dif_lvl > maximum:
                dif_lvl = 0
        except:
            continue
    return dif_lvl

def choosing_word(length_level):
    choosen_word = [random_word_from_file(words_file_path)]
    if length_level == 1:
        while len(choosen_word[0]) > 4:
            choosen_word[0] = random_word_from_file(words_file_path)
        return choosen_word[0]
    elif length_level == 2:
        while len(choosen_word[0]) < 5 and choosen_word[0] > 7:
            choosen_word[0] = random_word_from_file(words_file_path)
        return choosen_word[0]
    else:
        while len(choosen_word[0]) < 8:
            choosen_word[0] = random_word_from_file(words_file_path)
        return choosen_word[0]

def play(word, lifes):
    guess_table = []
    word_tmp = word.copy()

    win = False
    
    for i in word:
        guess_table.append("_")
    
    while lifes > 0:
        clear()
        if guess_table == word:
            print(" ".join(guess_table))
            print("********************\n--== YOU WIN ==--\n********************")
            lifes = 0
            win = True
            continue
        print_hangman(lifes)
        print(" ".join(guess_table))
        user_letter = input("Type a letter ('quit' to close): ")
        if user_letter.lower() == "quit":
            close()
        elif user_letter.lower() in word or user_letter.upper() in word:
            for i in word_tmp:
                cur_index = word_tmp.index(i)
                if cur_index == 0 and (word_tmp[cur_index] == user_letter.lower() or word_tmp[cur_index] == user_letter.upper()):
                    guess_table[cur_index] = user_letter.upper()  
                    word_tmp[cur_index] = "12@^t1gW"      
                elif word_tmp[cur_index] == user_letter.casefold():
                    guess_table[cur_index] = user_letter.lower()
                    word_tmp[cur_index] = "12@^t1gW"  
                else:
                    continue
        else:
            lifes -= 1

    if lifes == 0 and win == False:
        clear()
        print_hangman(lifes)

def main():
    lifes = choose_difficulty("amount of lifes", 3, 9)
    length_lvl = choose_difficulty("word length level", 1, 3)
    word = []
    word[:0] = choosing_word(length_lvl)

    play(word, lifes)

if __name__ == "__main__":
    while True:
        main()
        play_again = input("Do you want to play again? Y / N")
        if play_again.upper() == "Y":
            continue
        else:
            close()