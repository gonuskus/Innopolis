import time
import random

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
        print("Это был славный бой! Всего убитых чудищ - {0}.".format(monster_counter))
        print('Мы будем слагать о тебе легенды!')
    else:
        print("После боя у тебя осталось жизненных силушек - {0} шт.".format(hp, attack))
        print("Всего убитых чудищ - {0}.".format(monster_counter))


def apple():
    print("На пути нашем оказалась Яблоня Силу Дарующая!")
    print('БОГАТЫРЬ! Надо есть!')
    secret_number = random.randint(1, 5)
    global hp  # текущее состояние здоровье героя
    hp = hp + secret_number
    print("ЯБЛОЧКО принесло тебе жизненных силушек - {0} шт. Всего у тебя жизненных силушек - {1} шт.".format(
        secret_number, hp))
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
        "Богатырь, нам предстоит БОЙ! У Чудища {0} жизней, а в кулаках {1} кратная сила удара прячется".format(
            monster_health, monster_power))
    print("Крепко подумай богатырь! У тебя {0} жизненных силушек, а в мече твоем {1} мощных ударов.".format(hp, attack))
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
        "Не земле лежит ничейный МЕЧ, а в нем прячется {0} кратная сила удара".format(secret_number))
    print("Прими правильный выбор! В твоем мече {0} кратная сила удара.".format(attack))
    print("1 - взять меч себе выбросив старый")
    print("2 - пройти мимо меча")
    print("Каков твой выбор?")
    choice = input_validation(input())
    if choice == '2':
        print("Ты выбрал пройти мимо меча, так продолжим же наше путешествие!")
        print("Твой МЕЧ по прежнему содержит {0} кратную силу удара".format(attack))
    else:
        print("Отличный выбор!")
        attack = secret_number
        print("Новый МЕЧ обладает {0} кратной силой удара.".format(attack))


def game():
    global hp  # текущее состояние здоровье героя
    global attack  # текущая сила удара героя
    global monster_counter  # счетчик поверженных героем чудовищ
    global game_failed  # статус игры

    print("Привет, мой Богатырь! Я - боевой конь Юлий. У нас с тобой особое задание от самого Князя Киевского!", "\n",
          "Мы должны сразиться и победить 10 Чудищ Заморских!", '\n',
          "Я буду тебя сопровождать и давать полезные советы в нашем путешествии!")
    print("БОГАТЫРЬ! У тебя {0} жизненных силушек, а меч твой обладает {0} кратной силой удара.".format(hp, attack))

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
        print("Игра пройдена за {0} уровней".format(i))
        print('Конец Игры')


game()
