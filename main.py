import time
import parserr
import db_driver
import parser_onliner
import os.path

if not os.path.exists('db_main.db'):
    db_driver.db_create()
try:
    parserr.Parser().db_filling()
except:
    print('clone')
time.sleep(120)
# print('Старт поиска')
while True:
    try:
        parser_onliner.search()
    except:
        print('Search error')

#####
#Для работы нужно запустить ✔main.py подождать 120 секунд после ✔Bot_tg.py и зайти в телеграмм--->>> ✔@Aladin_mf_bot
# #таблица создастся автоматически + заполнится уже существующими объявлениями и туда постоянно будут добавляться новые квартиры по категориям
# в телеграмм после выбора категории придет 10 последних объявлений, а дальше будут приходить новое объявления о квартирах из выбранной категории
# примерно через +-3 секунды после публикации на сайте

#Для проверки нужно отсортировать на онлайнере квартиры по параметру (новые)