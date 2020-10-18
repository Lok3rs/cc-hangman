import os
import sys
import random
from typing import List
from print_hangman import *

''' Ustala scieżke relatywną '''
def get_file_path(file_name):
    return os.path.join(os.getcwd(), file_name)


''' Użytkownik wybiera ilość żyć z przedziału 3-8, funkcja w pętli do właściwego wyboru, lub 0 aby wyjść '''
def choose_lives() -> int:
    while True:
        try:
            user_life = int(input("Choose lives level (3-8), or 0 to quit:\n-->  "))
            if 3 <= user_life <= 8:
                return user_life
            elif user_life == 0:
                sys.exit("Thanks for playing!\n See you again!")
        except ValueError:
            os.system("clear || cls")
            get_logo()
            continue

''' Otwiera plik txt z nazwami państw i stolic, tworzy listę stringów '''
def get_list_of_words_from_file(path) -> List[str]:
    with open(path) as words:
        return [line.replace("\n", "") for line in words]

'''
Użytkownik wybiera poziom trudności w zależności od długości słów,  
na podstawie wyboru losuje jeden str, który będzie słowem do odgadnięcia
'''
def get_random_word_from_list() -> str:
    get_logo()
    input_ranges = {'1': (1, 4), '2': (5, 9), '3': (9, 16)}
    words = get_list_of_words_from_file(get_file_path('countries-and-capitals.txt'))
    while True:
        try:
            user_level = input("Choose word level between 1-3\n1. up to 4 letters\n2. 5-8 letters\n3. 9-16 letters\nor 0 to quit:\n--> ")
            if user_level == "0":
                sys.exit("Thanks for playing!\n See you again!")
            min_letters, max_letters = input_ranges[user_level]
            words_with_chosen_criteria = [word for word in words if min_letters <= len(word) <= max_letters]
            return random.choice(words_with_chosen_criteria)
        except KeyError:
            os.system("clear || cls")
            get_logo()

'''
Funkcja po zakończeniu rundy, niezależnie czy była wygrana, pyta użytkownika czy chce grać dalej, 
czy czy chce wyjść z programu.
'''
def play_again() -> None:
    ask_user = input("Do you want to play again? Y / N ")
    if ask_user.upper() == "Y":
        os.system("clear || cls")
        play(word=get_random_word_from_list(), lives=choose_lives())
    else:
        sys.exit("Thanks for playing!\n See you again!")

'''
Główna funkcja gry, użytkownik odgaduje literę bądź słowo:
- zakrywa losowe słowo do odgadnięcia
- drukuje liczbę żyć; próbowane litery bądź słowa, informacje o wygranej bądź przegranej
- wyjście za pomocą str ‘quit’,
- powiększa pierwszą literę w losowym str , jeśli użytkownik wpisze poprawnie cały
- zastępuje zakryte litery, trafionymi przez użytkownika 
'''
def play(word: str, lives: int) -> None:
    os.system("clear || cls")
    print(word)
    word_complete = "_" * len(word)
    print_word_complete = []
    for letter in word_complete:
        print_word_complete.append("_")
    win = False
    tried_letters = []
    print(f"{word} - for testing")  # for testing
    print(f"Lets play!\nTo exit game type: quit")
    print(print_hangman(lives))
    print(" ".join(print_word_complete))

    while not win and lives > 0:
        user_input = input(f"\nGuess letter or word: ")
        user_input = user_input.lower()
        os.system("clear || cls")

        if user_input == "quit":
            sys.exit("Thanks for playing!\n See you again!")

        if user_input.capitalize() == word:
            win = True
            break

        if user_input in tried_letters:
            print(f"You have already tired: '{user_input}'")

        elif user_input not in word.lower():
            print(f"Sorry - '{user_input}' - is not in the word")
            lives -= 1
            tried_letters.append(user_input)

        else:
            print(f"Great - '{user_input}' - is in the word")
            tried_letters.append(user_input)

            for letter in range(len(word)):
                if word[letter].lower() == user_input.lower():
                    word_complete = f"{word_complete[:letter]}{word[letter]}{word_complete[letter + 1:]}"

            if "_" not in word_complete:
                win = True

        print(print_hangman(lives))
        print(f"Tried: {tried_letters}")
        print("To exit game type: quit")
        print_word = []
        for letter in word_complete:
            print_word.append(letter)
        print(" ".join(print_word))

    if win:
        result = "WON!"
    else:
        result = "LOST!"

    os.system("clear || cls")
    print(print_hangman(lives))
    print(f"********************\n--== YOU {result} ==--\nThe word is: {word}\n********************")
    play_again()


if __name__ == '__main__':
    while True:
        os.system("clear || cls")
        word = get_random_word_from_list()
        lives = choose_lives()
        play(word=word, lives=lives)