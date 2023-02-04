# Виселица

from random import *

people_list = ["человек", "женщина", "личность", "ребенок"]
work_list = ["работа", "начальник", "сотрудник"]
politics_list = ["власть", "правительство", "экономика", "развитие", "граница", "председатель", "республика"]
word_list = people_list + work_list + politics_list

def category_word(word, work_list, politics_list):
    if work_list.count(word) + work_list.count(word.lower())> 0:
        category = 'Слово из категории: работа'
    elif politics_list.count(word) + politics_list.count(word.lower())> 0:
        category = 'Слово из категории: политика'
    else:
        category = 'Слово из категории: человек'
    return category

def get_word():
    return choice(word_list).upper()

def display_hangman(tries):
    stages = [
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
             # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                  # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def print_word(word, list):
    for c in word:
        if c in list:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()

def play(word):
    word_completion = word[0] + '_' * (len(word) - 2) + word[-1]  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    print('Давайте играть в угадайку слов!')
    print(word_completion)
    print(display_hangman(tries))
    print(category_word(word, work_list, politics_list))

    while True:
        letter_input = input('Введите букву кириллического алфавита: \n').upper() 
        if not letter_input.isalpha():
            print('Ошибка ввода. Попробуйте снова')
            continue
        if letter_input in guessed_letters or letter_input in guessed_words:
            print('Слово/буква уже было')
        if len(letter_input) > 1:
            if letter_input == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
            else:
                guessed_words.append(letter_input)
                tries -= 1
                print(f'Не верно, осталось попыток {tries}')
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                if tries == 0:
                    print(f'Вы не смогли угадать слово: {word}')
                    break
                continue
        
        if letter_input in word:
            guessed_letters.append(letter_input)
            for c in word:
                if c not in guessed_letters:
                    print('Угадали букву')
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:    
                print_word(word, guessed_letters)
                print('Поздравляем, вы угадали слово! Вы победили!')
                break        
        else:
            guessed_letters.append(letter_input)
            tries -= 1
            print(f'Не верно, осталось попыток {tries}')
            print(display_hangman(tries))
            print_word(word, guessed_letters)
        if tries == 0:
            print(f'Вы не смогли угадать слово: {word}')
            break

def main_game():
    play(get_word().upper())
    continue_game = input('Хотите продолжить? Нажмите клавишу "д" чтобы сыграть ещё раз, или клавишу "н" чтобы выйти. \n')
    while True:
        if continue_game.upper() == 'Д':
            play(get_word().upper())
        if continue_game.upper() == 'Н':
            break
        else:
            continue_game = input('Хотите продолжить? Нажмите клавишу "д" чтобы сыграть ещё раз, или клавишу "н" чтобы выйти. \n')
            continue    

main_game()
