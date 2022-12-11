import requests
import db_driver
import time
from random import randint

fundamental_address = "https://r.onliner.by/sdapi/ak.api/search/apartments"


# root_get = requests.get(fundamental_address)
# root_resault = root_get.json()
# print(root_resault)
####link_photo, time_create, price_usd, price_byn, room, address, link_apartment, coordinates, owner####
class Parser():
    def db_filling(self):
        for page in range(1, 16):
            time.sleep(3 + randint(1, 3))
            options = {'page': page, 'order': 'created_at:desc'}

            # 'rent_type[]': room, 1_room, 2_room, 3_room
            # 'only_owner': 'true' if 'false' -> remove 'only_owner' from dictionary
            # 'order': 'created_at:desc' -> new
            # 'order':  'price:asc'      -> cheap
            # 'order':  'price:desc'     -> expensive
            # when none order            -> topical
            # options['page'] = page

            flats = requests.get(fundamental_address, options)
            res = flats.json()
            for slice_root in list(range(len(res['apartments']))):
                Parser().pars(slice_root, res)

    def pars(self, slice_root, res):
        # нужно добавить отсееватель по ссылке если есть объява <----------
        #----------------------------------------------------------------------
            link_photo = res['apartments'][slice_root]['photo']  # link_photo
            time_create = res['apartments'][slice_root]['created_at']  # time_create
            price_usd = res['apartments'][slice_root]['price']['converted']['USD']['amount']  # price_usd
            price_byn = res['apartments'][slice_root]['price']['converted']['BYN']['amount']  # price_byn
            room = res['apartments'][slice_root]['rent_type'][0]  # room
            address = res['apartments'][slice_root]['location']['user_address']  # address
            link_apartment = res['apartments'][slice_root]['url']  # link_apartment
            coordinates = str(res['apartments'][slice_root]['location']['latitude']) + ',' + str(
                res['apartments'][slice_root]['location']['longitude'])  # coordinates
            owner = res['apartments'][slice_root]['contact']['owner']  # owner
            db_driver.db_add(link_photo, time_create, price_usd, price_byn, room, address, link_apartment,
                             coordinates,
                             owner)


if __name__ == "__main__":
    Parser().db_filling()  # padding with initial values
