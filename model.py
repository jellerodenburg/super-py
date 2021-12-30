class Product:
    def __init__(self, id, name, buy_date, buy_price, expiration_date):
        self.id = id
        self.name = name
        self.buy_date = buy_date
        self.buy_price = buy_price
        self.expiration_date = expiration_date

    def __repr__(self) -> str:
        return "Product(id: {}, name: {}, buy_date: {}, buy_price: {}, expiration_date: {})".format(
            self.id, self.name, self.buy_date, self.buy_price, self.expiration_date
        )


class Sale:
    def __init__(self, id, bought_id, sell_date, sell_price):
        self.id = id
        self.bought_id = bought_id
        self.sell_date = sell_date
        self.sell_price = sell_price

    def __repr__(self) -> str:
        return "Sale(id: {}, bought_id: {}, sell_date: {}, sell_price: {})".format(
            self.id, self.bought_id, self.sell_date, self.sell_price
        )
