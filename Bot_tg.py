import time
import telebot
from telebot import types
import sqlite3

# from threading import Thread
# from publication import Bot_t


bot = telebot.TeleBot('5877083240:AAHDpvXM-EMZIY20gEO4bIBmLGS_Gi467yA')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item0 = types.KeyboardButton("Просто комната")
    item1 = types.KeyboardButton("1 комнатная")
    item2 = types.KeyboardButton("2 комнатная")
    item3 = types.KeyboardButton("3 комнатная")
    item4 = types.KeyboardButton("4 комнатная")
    markup.add(item0)
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)

    bot.send_message(m.chat.id,
                     'Нажми: \n Какую квартиру вы хотите найти? ',
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    def agent(message):

        if message == 1:
            return 'Собственник'
        else:
            return 'Агент'

    def bot_mess(res_message):
        armagedon = f'{res_message[0][1]} \n {res_message[0][2][11:19]}--{res_message[0][2][:10]} \n {res_message[0][3]} USD {res_message[0][4]} BYN \n Комнат : {res_message[0][5]}  {agent(res_message[0][9])} \n Адрес: {res_message[0][6]} \n {res_message[0][7]}'
        bot.send_message(message.chat.id, armagedon)

    def bot_pub_newf(room):
        connect = sqlite3.connect('db_main.db', check_same_thread=False)
        cursor_bot_t = connect.cursor()
        cursor_bot_t.execute(f'''SELECT time_create FROM {room}  ORDER BY time_create DESC''')
        res = cursor_bot_t.fetchall()
        res_get = res[:10]
        for i in res_get[::-1]:
            cursor_bot_t.execute(f'''SELECT * FROM {room} WHERE  time_create = '{i[0]}' ''')
            res_message = cursor_bot_t.fetchall()
            bot_mess(res_message)
        a = True
        while a:
            if message.text.strip() in ['Просто комната', '1 комнатная', '2 комнатная', '3 комнатная', '4 комнатная']:
                a = False


            time.sleep(1)
            cursor_bot_t.execute(f'''SELECT time_create FROM {room}  ORDER BY time_create DESC''')
            res_while_true = cursor_bot_t.fetchall()
            res_get_while = set(res_while_true[:10])

            res_set = res_get_while - set(res_get)
            res_get = res_get_while.copy()
            # print(res_set)
            if len(res_set) > 0:
                res_set = sorted(list(res_set))
                for e in res_set:
                    cursor_bot_t.execute(f'''SELECT * FROM {room} WHERE  time_create = '{e[0]}' ''')
                    res_message_new = cursor_bot_t.fetchall()
                    bot_mess(res_message_new)

    if message.text.strip() == 'Просто комната':
        message.text = ''
        bot_pub_newf('room')
    elif message.text.strip() == '1 комнатная':
        message.text = ''
        bot_pub_newf('room_1')
    elif message.text.strip() == '2 комнатная':
        message.text = ''
        bot_pub_newf('rooms_2')
    elif message.text.strip() == '3 комнатная':
        message.text = ''
        bot_pub_newf('rooms_3')
    elif message.text.strip() == '4 комнатная':
        message.text = ''
        bot_pub_newf('rooms_4')


bot.polling(none_stop=True, interval=0)
