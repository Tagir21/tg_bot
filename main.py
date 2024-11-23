import telebot
import schedule
from threading import Thread
import time
from datetime import datetime
from multiprocessing.context import Process

from random import randint

bot = telebot.TeleBot('7940109673:AAFXwqcP386ahTjV-kmkKJnWg-zrxgWepsw')


array_of_horoscope = [
    'Сегодня неожиданные повороты ситуации (включая странные поступки старых друзей, капризы детей и оригинальные причуды любимого человека) не слишком удивят Козерогов и не станут для них источником фатальных огорчений. Наоборот, многие Козероги найдут для себя в событиях дня некую выгоду, например, возможность заработать, обновить часть своей жизни или закрыть какую-то страницу в своей биографии',
    'Сегодня Водолеи могут чаще обычного сталкиваться с капризами близких или с побочными эффектами своих нестандартных бытовых привычек. Непросты и отношения с внешним миром (в том числе, с целевой большой аудиторией, если планируется публичная карьера). Одной из проблем дня может оказаться свободолюбие. Возможен неожиданный поворот в общении с начальством, партнером, друзьями, детьми или родителями.',
    'Сегодня внимание Рыб может привлечь поведение старого друга, родственника или авторитетного лица. Независимо от расстояния, разделяющего их с этим человеком, его позиция может иметь для них большое значение, быть ценным ориентиром или демотиватором. Рутинные дела в эти сутки пойдут не без сюрпризов. Нежелательно планировать на сегодня ответственные мероприятия, включая сделки и целевые поездки.',
    'Этот день способен подтолкнуть Овнам к неожиданным финансовым решениям и экстравагантным тратам, усилить их интерес к новинкам. Также сегодня для них возрастает риск столкнуться с нетипичным или ненадежным поведением других людей, имеющих отношение к их деньгам или ресурсам. Может неожиданно повести себя друг, созаемщик, продавец, покупатель, кредитор. В эти сутки лучше воздержаться от сделок.',
    'Сегодня для Тельцов возрастает вероятность сюрпризов, волнений и необычных переживаний. Для многих Тельцов источником бурных эмоций станет поведение конкретного человека, с которым они связаны узами любви, дружбы или делового сотрудничества. У большинства Тельцов будет при этом точка опоры, благодаря которой они не утратят душевного равновесия. День может стать важным для значимых отношений',
    'Сегодня Близнецы могут оказаться наблюдателями перипетий чужой жизни или быть втянуты в нее лично (что зависит не столько от их воли, сколько от нюансов карты рождения). В обоих случаях они получат неожиданные впечатления, например, узнают с нетипичной стороны своего друга, коллегу или помощника. Близнецам, попавшим в нештатную ситуацию, не помешает финансовая поддержка, материальный резерв.',
    'Сегодня внимание Раков могут привлечь социальные процессы или события в кругу друзей, так или иначе связанные с их собственным будущим (особенно в его материально-экономической части). Может вызвать интерес поведение конкретного человека или организации. На этом фоне возрастет ценность брака, старинной дружбы или устоявшегося партнерства, сочетающего в себе признаки официального и неформального.',
    'События этого дня для Львов сродни мини-революции, но не все особенности ситуации будут для них сюрпризом: многие тенденции уже были известны заранее и вполне очевидны. Тем не менее, в течение дня возможны волнения и неожиданности. Могут частично измениться виды на будущее, претерпеть трансформацию отношения со значимыми персонами, профессиональные планы или отдельные элементы бытового уклада.',
    'Сегодня звезды советуют Девам не упускать из виду социальный фон и события в обществе, в том числе, на отдаленных территориях. Что-то важное может происходить в жизни далеких друзей, бывших учителей, авторитетных персон, дальних родственников или зарубежных коллег. Особенно внимательными стоит быть Девам, которых волнует материальный вопрос (жилье, недвижимость, право собственности, заработок).',
    'Весам звезды подсказывают, что сегодня день материальных и других сюрпризов - которые, при определенных дополнительных условиях, могут стать роковыми для любви, дружбы, доходов или бизнеса. Не слишком предсказуем исход новых чувства, сделок и вложений, зато могут настигнуть последствия опрометчивых экспериментов прошлого. Возможен неожиданный поворот в истории с долгом, кредитом или наследством.',
    'Этот день значим для отношений Скорпионов с конкретными людьми. В завимости от ситуации, на первый план может выйти дружба, брачный союз, деловое сотрудничество или творческий тандем. Также может стать важной расстановка сил в ситуации соперничества. Для некоторых Скорпионов будет важнее их репутация в группе или позиция в коллективе, право на оригинальность, на долю свободы и независимости.',
    'Сегодня Стрельцов могут ждать нештатные ситуации на работе, в связи с финансовыми делами или здоровьем. В течение дня возможны отступления от привычного расписания, диеты, бюджета или бытового уклада, зато возможен сюрприз, эксперимент или нововведение. Может удивить каприз питомца, нетипичное поведение друга, помощника, врача, кредитора или должника, представителя учреждения или сообщества.'
]

# Словарь для каждого пользователя по отложенному сообщению
users_shed = {}
# Словарь по игрокам которые играют
users_play = {}


def random_horoscope_f():
    with open('horoscopes.txt', 'r', encoding='utf-8') as f:
        arr_file = f.readlines()

        return arr_file[randint(0, 11)]

#Обработчик очереди
def run_schedule_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)

@bot.message_handler(commands=['start'])
def random_horoscope(message):
    bot.send_message(message.chat.id, array_of_horoscope[randint(0, 11)])
    bot.send_message(message.chat.id, 'Чтобы подписаться на рассылку гороскопов - введи /horoscope')
    stat(message)

@bot.message_handler(commands=['play'])
def word_game(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Вам необходимо указать два знака зодиака через пробел (например: Весы Лев)')
    bot.send_message(chat_id, 'Чтобы остановить игру напишите - скорпион')
    users_play[chat_id] = True #Инициализируем id игрока
    stat(message)
#Запускаем игру
@bot.message_handler(func=lambda message: message.chat.id in users_play and users_play[message.chat.id] == True)
def word_answer(message):
    chat_id = message.chat.id
    if message.text == 'скорпион':
        users_play[chat_id] = False
        bot.send_message(chat_id, 'Игра остановлена, чтобы начать игру заново напишите /play')
    else:
        try:
            sign1, sign2 = message.text.split()
            bot.send_message(chat_id, f'Совместимость {sign1} и {sign2} - {randint(0, 100)}%')
        except ValueError:
            bot.send_message(chat_id, 'Неверный формат ввода, пожалуйста укажите два знака зодиака через пробел')
    stat(message)
#Отправка отложенных сообщений
@bot.message_handler(commands=['horoscope'])
def every_hour(message):
    chat_id = message.chat.id
    if (chat_id in users_shed) and (len(schedule.get_jobs(str(chat_id))) > 0):
        bot.send_message(chat_id, 'Гороскоп уже включён, чтобы выключить - "/stop_horoscope"')
    else:
        #Бот отправляет рандомный гороскоп из файла каждый час, чтобы посмотреть работу можно поменять hour на minute
        schedule.every().hour.do(lambda : bot.send_message(chat_id, random_horoscope_f())).tag(str(chat_id))
        users_shed[chat_id] = True
        bot.send_message(chat_id, 'Гороскоп включён')
    stat(message)
#Функция очистки очереди
@bot.message_handler(commands=['stop_horoscope'])
def stop(message):
    chat_id = message.chat.id
    if (chat_id in users_shed) and (len(schedule.get_jobs(str(chat_id))) > 0):
        schedule.clear(str(chat_id))
        del users_shed[chat_id]
        bot.send_message(chat_id, 'Гороскоп выключен')
    else:
        bot.send_message(chat_id, 'Что - то пошло не так')
    stat(message)
@bot.message_handler(func=lambda message: True)
def stat(message):
    with open("log.txt", 'a') as f:
        f.write(f"{message.text}\n")

if __name__ == '__main__':
    scheduleThread = Thread(target=run_schedule_tasks)
    scheduleThread.daemon = True
    scheduleThread.start()
    bot.polling(none_stop=True)
