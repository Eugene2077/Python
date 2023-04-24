
class Product:
    def __init__(self,price):
        self.set_price(price)

    def get_price(self):
        return self.__price     # 이 부분 이해안감

    def set_price(self,value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value    # 여기도 이해안감