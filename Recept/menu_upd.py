from bd import Menu, session
from datetime import datetime


schedule = {0: {'Borsh': 200},
            1: {'Solyanka': 500},
            2: {'Chicken': 500},
            3: {'Bread': 500},
            4: {'Ramen': 500},
            5: {'Soup': 500},
            6: {'Coffee': 500}
            }


def menu_update():
    while True:
        print("start")
        if session.query(Menu.name).first() is None:
            key = list(schedule[datetime.today().weekday()].items())[0]
            menu = Menu(name=key[0], price=[1][0])
            session.add(menu)
            session.commit()
        if datetime.now().time().hour == 0:
            key = list(schedule[datetime.today().weekday()].items())[0]
            session.query(Menu).delete()
            menu = Menu(name=key[0], price=[1][0])
            session.add(menu)
            session.commit()


if __name__ == "__main__":
    menu_update()

