import random
from random import choice
from colorama import init
from colorama import Fore, Back, Style
def file_open(filename):
    with open(filename, encoding='utf-8') as file:
        words = [*filter(lambda x: x[:-1].lower() if len(x.strip()) == 5 else None, file.readlines())]
        sp = [word.strip() for word in words if '\n' in word]
    return sp
def write_word():
    a = input("Введите ваше слово \n").strip()
    return a
def Wordle():
    init()
    sp = file_open('words.txt')
    alphabet = ""
    cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_top = ""
    alphabet_mid = ""
    alphabet_bot = ""
    stroka = "\n"
    for i in range(len(list(cyrillic_lower_letters))):
        if cyrillic_lower_letters[i] not in alphabet:
            alphabet_top += Back.BLACK + Fore.LIGHTWHITE_EX + "┌─┐" + Back.RESET + Fore.RESET + " "
            alphabet_mid += Back.BLACK + Fore.LIGHTWHITE_EX + f"│{cyrillic_lower_letters[i]}│" + Back.RESET + Fore.RESET + " "
            alphabet_bot += Back.BLACK + Fore.LIGHTWHITE_EX + "└─┘" + Back.RESET + Fore.RESET + " "
    alphabet+=alphabet_top+"\n"+alphabet_mid+"\n"+alphabet_bot+stroka
    print("Все доступные буквы".rjust(75," "))
    print(alphabet)
    our_word = choice(sp)
    list_letters = list(our_word)
    print("\t\t"+Back.GREEN+Fore.BLACK+"Суть игры Wordle"+Back.RESET+Fore.RESET)
    print("\n"+Back.GREEN+Fore.BLACK+"Ваша задача за 6 попыток отгадать слово из пяти букв.Все буквы строчные."+Back.RESET+Fore.RESET)
    print("\n"+Back.YELLOW + Fore.BLACK+"А"+Back.RESET + Fore.RESET+"-Цвет буквы, если буква есть в слове и стоит на этой же позиции")
    print("\n"+Back.LIGHTWHITE_EX + Fore.BLACK + "Б" + Back.RESET + Fore.RESET+"-Цвет буквы, если буква есть в слове, но не на этой конкретной позиции")
    print("\n"+Back.BLACK + Fore.LIGHTWHITE_EX + "В" + Back.RESET + Fore.RESET + "-Цвет буквы,если буквы нет в слове    ")
    #print("\nЗагадано слово:",Back.LIGHTWHITE_EX + Fore.MAGENTA + our_word+Back.RESET+Fore.RESET)
    #Проверка тест
    game_end = False
    #fd
    attempts = 6
    word = ""
    while game_end != True:
        top_row = ""
        mid_row = ""
        bot_row = ""
        print(f"Количество попыток" + Fore.RED + f" {attempts}" + Fore.RESET)
        if attempts == 0:
            print(Fore.RED + "К сожалению, попытки закончились. Вы не угадали слово." + Fore.RESET)
            print(f"Загаданное слово было: {Back.LIGHTWHITE_EX + Fore.CYAN + our_word + Fore.RESET + Back.RESET}")
            break
        input_word = write_word().lower()
        while input_word not in sp or len(input_word)!=5:
            print("\nВы ввели слово меньше 5 букв или слово, которого нету в базе данных")
            attempts -= 1
            print(f"Количество попыток" + Fore.RED + f" {attempts}" + Fore.RESET)
            if attempts == 0:
                print(Fore.RED + "К сожалению, попытки закончились. Вы не угадали слово." + Fore.RESET)
                print(f"Загаданное слово было: {Back.LIGHTWHITE_EX + Fore.MAGENTA + our_word + Fore.RESET + Back.RESET}")
                game_end = True
                break
            input_word = write_word()
        if game_end ==True:
            break
        if attempts != 0:
            """
            alphabet=list(alphabet)
            for index in range(len(alphabet)):
                if index < len(input_word) and alphabet[index] == input_word[index]:
                    alphabet[index] = Back.YELLOW + Fore.BLACK + f"{alphabet[index]}" + Back.RESET + Fore.RESET
                elif alphabet[index] in input_word:
                    alphabet[index] = Back.WHITE + Fore.BLACK + f"{alphabet[index]}" + Back.RESET + Fore.RESET
                else:
                    alphabet[index] = Back.LIGHTBLACK_EX + Fore.WHITE + f"{alphabet[index]}" + Back.RESET + Fore.RESET
            """
            for index in range(len(input_word)):
                if input_word[index] == list_letters[index]:
                    top_row += Back.YELLOW + Fore.BLACK + "┌─┐" + Back.RESET + Fore.RESET + " "
                    mid_row += Back.YELLOW + Fore.BLACK + f"│{input_word[index]}│" + Back.RESET + Fore.RESET + " "
                    bot_row += Back.YELLOW + Fore.BLACK + "└─┘" + Back.RESET + Fore.RESET + " "
                elif input_word[index] != list_letters[index] and input_word[index] in list_letters:
                    top_row += Back.LIGHTWHITE_EX + Fore.BLACK + "┌─┐" + Back.RESET + Fore.RESET + " "
                    mid_row += Back.LIGHTWHITE_EX + Fore.BLACK + f"│{input_word[index]}│" + Back.RESET + Fore.RESET + " "
                    bot_row += Back.LIGHTWHITE_EX + Fore.BLACK + "└─┘" + Back.RESET + Fore.RESET + " "
                else:
                    top_row += Back.BLACK + Fore.LIGHTWHITE_EX + "┌─┐" + Back.RESET + Fore.RESET + " "
                    mid_row += Back.BLACK + Fore.LIGHTWHITE_EX + f"│{input_word[index]}│" + Back.RESET + Fore.RESET + " "
                    bot_row += Back.BLACK + Fore.LIGHTWHITE_EX + "└─┘" + Back.RESET + Fore.RESET + " "
            word += top_row + "\n" + mid_row + "\n" + bot_row + stroka
            print(alphabet)
            print(word)
        if input_word == our_word:
            print(Fore.BLUE + "Победа, вы угадали слово!" + Fore.RESET)
            game_end = True
            break

        if attempts == 0:
            print(Fore.RED + "К сожалению, попытки закончились. Вы не угадали слово." + Fore.RESET)
            print(f"Загаданное слово было: {Back.LIGHTWHITE_EX + Fore.BLACK + our_word + Fore.RESET + Back.RESET}")
            break
        attempts -= 1

if __name__ == "__main__":
    Wordle()