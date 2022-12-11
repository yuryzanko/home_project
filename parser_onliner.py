import requests
import parserr
import time
from random import randint
import sqlite3


def search():
    room_root = {'r': 'room', '1': 'room_1', '2': 'rooms_2', '3': 'rooms_3', '4': 'rooms_4'}

    fundamental_address = "https://r.onliner.by/sdapi/ak.api/search/apartments"
    time.sleep(3 + randint(1, 3))
    options = {'page': 1, 'order': 'created_at:desc'}
    flats = requests.get(fundamental_address, options)
    res_from_site = flats.json()
    # print(res_from_site)
    db_main = sqlite3.connect("db_main.db")
    cursor_db = db_main.cursor()

    for site_value in reversed(range(15)):
        link_apartment = res_from_site['apartments'][site_value]['url']
        room = res_from_site['apartments'][site_value]['rent_type'][0]
        # print(link_apartment)
        # print(room)
        res_search = cursor_db.execute(
            f'''SELECT * FROM {room_root[room]} WHERE  link_apartment = '{link_apartment}' ''')
        res_search_decoded = res_search.fetchall()
        # print(res_search_decoded)
        if len(res_search_decoded) == 0:
            # print(link_apartment)
            parserr.Parser().pars(site_value, res_from_site)
        else:
            continue


if __name__ == "__main__":
    while True:
        search()
