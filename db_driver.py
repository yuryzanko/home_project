import sqlite3


def db_create():
    db_main = sqlite3.connect("db_main.db")
    cursor_db = db_main.cursor()
    list_rooms = ['', '_1', 's_2', 's_3', 's_4', 's_5', 's_6']
    for n in list_rooms:
        room = f'room{n}'
        cursor_db.execute(
            f'''CREATE TABLE IF NOT EXISTS {room}(id INTEGER PRIMARY KEY AUTOINCREMENT, link_photo, time_create,
            price_usd REAL, price_byn REAL, room, address, link_apartment UNIQUE, coordinates, owner)''')
    cursor_db.close()


if __name__ == "__main__":
    db_create()            # create table


def db_add(link_photo, time_create, price_usd, price_byn, room, address, link_apartment, coordinates, owner):
    if address[:5] == 'Минск':
        db_main = sqlite3.connect("db_main.db")
        cursor_db = db_main.cursor()
        room_root = {'r': 'room', '1': 'room_1', '2': 'rooms_2', '3': 'rooms_3', '4': 'rooms_4'}
        if room in room_root.keys():
            table = room_root[room]
            cursor_db.execute(f'insert into {table} (link_photo, time_create, price_usd, price_byn, room, address,'
                              f'link_apartment, coordinates, owner) values(?, ?, ?, ?, ?, ?, ?, ?, ?)',
                              (
                                  link_photo, time_create, price_usd, price_byn, room, address, link_apartment,
                                  coordinates,
                                  owner))
            db_main.commit()
            cursor_db.close()
