from bd import session, Menu, Order, Items


class CommonAction:
    @staticmethod
    def add(name, items):
        if set(items).issubset(list(map(''.join, session.query(Menu.name).all()))):
            if name not in list(map(''.join, session.query(Order.name).all())):
                order = Order(name=name, price=0)
                session.add(order)
                session.commit()
            order = session.query(Order).filter(Order.name == name).first()
            for item in items:
                CommonAction.items_append(item, order, name)

    @staticmethod
    def items_append(item, order, name):
        it = Items(name=item, price=session.query(Menu.price).filter(Menu.name == item).first()[0])
        session.query(Order).filter(Order.name == name).update(
            {'price': session.query(Order.price).filter(Order.name == name).first()[0] +
                      session.query(Menu.price).filter(Menu.name == item).first()[0]})
        order.items.append(it)
        session.commit()

    @staticmethod
    def get_ordered_items(name):
        order = session.query(Order).filter(Order.name == name).first()
        if order is None:
            return []
        return list(map(''.join, session.query(Items.name).with_parent(order).all()))

    @staticmethod
    def get_menu():
        return [row._asdict() for row in session.query(Menu.name, Menu.price).all()]

