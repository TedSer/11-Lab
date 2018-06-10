from enum import Enum


class ItemBrand(Enum):
    LG = "LG"
    Pioneer = 'Pioneer'
    Sim = "Sim"


class Goods:

    def __init__(self, name, item_brand, price, amount):
        self.item_brand = item_brand
        self.price = price
        self.name = name
        self.amount = amount

    def __str__(self):
        return "Name :" + str(self.name) + "; Price " + str(self.price) + "; Item brand " + str(self.item_brand) \
               + "; Amount :" + str(self.amount)
