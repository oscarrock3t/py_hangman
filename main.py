import requests
from bs4 import BeautifulSoup

def msg(arg, hp=5):
    if arg == 'start':
        print('Здарова, сейчас ты будешь угадывать слово!\n'
              'Необходимо угадывать слово по буквам\n'
              'За 5 неправильных попыток приложение закроется!\n'
              'Поехали!\n')
    elif arg == 'err':
        print('Упс! Попробуй другую букву','Количетсво жизней:', hp)
    elif arg == 'lose':
        print('Конец!')
    elif arg == 'again':
        pass
    elif arg == 'win':
        print('Молодцом! Ты победил!')
    elif arg == 'succ_char':
        print('Верно!')


def generate_word():
    response = requests.get('https://calculator888.ru/random-generator/sluchaynoye-slovo')
    soup = BeautifulSoup(response.text, 'html.parser')
    a = soup.find_all('div', id='bov')
    return a[0].getText().lower()


def main():
    quest = generate_word()
    msg('start')
    health = 5
    quest_list = list(quest)
    user_list = ['_' for _ in range(len(quest_list))]
    while health != 0:
        print(*user_list)
        user_option = input()
        if user_option in quest_list:
            for idx, val in enumerate(quest_list):
                if val == user_option:
                    user_list[idx] = val
            msg('succ_char')
        else:
            health -= 1
            msg('err', health)
        if user_list == quest_list:
            msg('win', quest)
            break
    if health == 0:
        msg('lose')
    msg('end')
    print('Загаданное слово было:\n', quest.capitalize())


if __name__ == '__main__':
    main()