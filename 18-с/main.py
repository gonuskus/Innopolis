import random
import time

global hp  # текущее состояние здоровье героя
global attack  # текущая сила удара героя
global game_failed  # статус игры
global monster_counter
monster_counter = 0
hp = 10
attack = 10
game_failed = 0


def input_validation(string):
    choice = string
    while choice not in ['1', '2']:
        print('Богатырь, глаза подводят тебя! Ввести надо цифру, 1 или 2')
        print("1 - Да")
        print("2 - Нет")
        choice = input()
    return choice


def check_hp():
    global game_failed
    if hp <= 0:
        print('ПОРАЖЕНИЕ от нанесенных ран')
        game_failed = 1
        print(f"Это был славный бой! Всего убитых чудищ - {monster_counter}.")
        print('Мы будем слагать о тебе легенды!')
    else:
        print(f"После боя у тебя осталось жизненных силушек - {hp} шт.")
        print(f"Всего убитых чудищ - {monster_counter}.")


def apple():
    print("На пути нашем оказалась Яблоня Силу Дарующая!")
    print('БОГАТЫРЬ! Надо есть!')
    secret_number = random.randint(1, 5)
    global hp  # текущее состояние здоровье героя
    hp = hp + secret_number
    print(f"ЯБЛОЧКО принесло тебе жизненных силушек - {secret_number} шт. Всего у тебя жизненных силушек - {hp} шт.")
    time.sleep(2)


def monster():
    global hp  # текущее состояние здоровье героя
    global attack  # текущая сила удара героя
    global game_failed  # статус игры
    global monster_counter
    print("На пути нашем повстречалось Чудище! Да не простое!")
    monster_health = random.randint(10, 20)
    monster_power = random.randint(1, 10)
    print(
        f"Богатырь, нам предстоит БОЙ! У Чудища {monster_health} жизней, а в кулаках {monster_power} кратная сила "
        f"удара прячется")
    print(f"Крепко подумай богатырь! У тебя {hp} жизненных силушек, а в мече твоем {attack} мощных ударов.")
    print("1 - Ты решаешь принять бой")
    print("2 - Ты решаешь убежать")
    print("Каков твой выбор?")
    choice = input_validation(input())
    if choice == '2':
        print("Ты выбрал бегство, что ж разумно! Надо б сил поднабраться!")
    else:
        print("Ты выбрал принять бой! Да прибудет с тобой силушка богатырская!")
        time.sleep(1)
        print("И сошлись Богатырь да Чудище в бою неравном, в бою смертельном!")
        time.sleep(1)
        if attack > monster_health:
            print('Да одержал Богатырь победу над Чудищем!')
            monster_counter = monster_counter + 1
            hp = hp - monster_power
            check_hp()
            time.sleep(2)

        elif monster_health > attack:
            print('ПОРАЖЕНИЕ... Пал храбрый Богатырь... Чудище оказалось коварным')
            game_failed = 1
        else:
            print('Ничья! Надавал тумаков Богатырь наш. Да убежало Чудище окаянное в лес.')
            hp = hp - monster_power
            check_hp()
            time.sleep(2)


def sword():
    global attack  # текущая сила удара героя
    secret_number = random.randint(5, 20)
    print(
        f"Не земле лежит ничейный МЕЧ, а в нем прячется {secret_number} кратная сила удара")
    print(f"Прими правильный выбор! В твоем мече {attack} кратная сила удара.")
    print("1 - взять меч себе выбросив старый")
    print("2 - пройти мимо меча")
    print("Каков твой выбор?")
    choice = input_validation(input())
    if choice == '2':
        print("Ты выбрал пройти мимо меча, так продолжим же наше путешествие!")
        print(f"Твой МЕЧ по прежнему содержит {attack} кратную силу удара")
    else:
        print("Отличный выбор!")
        attack = secret_number
        print(f"Новый МЕЧ обладает {attack} кратной силой удара.")


def game():
    global hp  # текущее состояние здоровье героя
    global attack  # текущая сила удара героя
    global monster_counter  # счетчик поверженных героем чудовищ
    global game_failed  # статус игры

    print("Привет, мой Богатырь! Я - боевой конь Юлий. У нас с тобой особое задание от самого Князя Киевского!", "\n",
          "Мы должны сразиться и победить 10 Чудищ Заморских!", '\n',
          "Я буду тебя сопровождать и давать полезные советы в нашем путешествии!")
    print(f"БОГАТЫРЬ! У тебя {hp} жизненных силушек, а меч твой обладает {attack} кратной силой удара.")

    point = ''
    step = [monster, apple, sword]
    i = 0
    while monster_counter != 10 and game_failed != 1:
        i = i + 1
        print('Уровень ', i)
        while point != monster or point == '':
            print('Идем мы с Богатырем по землице Русской... Как вдруг!...')
            time.sleep(1)
            point = random.choice(step)
            point()
        point = ''
    if game_failed == 1:
        print('Конец Игры')

    if monster_counter == 10:
        print('ПОБЕДА! Киев-град спасен от нападения чудищ!')
        print(f"Игра пройдена за {i} уровней")
        print('Конец Игры')


game()
