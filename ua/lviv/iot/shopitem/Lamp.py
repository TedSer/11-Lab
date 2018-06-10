from ua.lviv.iot.shopitem.Goods import Goods


class Lamp(Goods):


    def __init__(self, name, item_brand, price, amount):
        super().__init__(name, item_brand, price, amount)


    def __str__(self):
        return Goods.__str__(self)