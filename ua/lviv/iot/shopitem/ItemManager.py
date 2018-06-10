from ua.lviv.iot.shopitem.Lamp import Lamp
from ua.lviv.iot.shopitem.Camera import Camera
from ua.lviv.iot.shopitem.Microphone import Microphone
from ua.lviv.iot.shopitem.Goods import ItemBrand


class Manager:
    items_brand = []

    listForDict = []

    a = {"key": listForDict}

    def find_by_item_brand(self, item_brand):
        foended_items = []

        for items in self.items_brand:
            if items.item_brand == item_brand:
                foended_items.append(items)
        return foended_items

    def sort_by_price(self):
        self.items_brand.sort(key=lambda items: items.price)
        return self.items_brand

    @staticmethod
    def print_list(printed_list):
        for items in printed_list:
            print(items)
        print("\n")


if __name__ == "__main__":
    lamp = Lamp("Sunshine ", ItemBrand.LG.value, 4000, 200)
    camera = Camera("4k.boost ", ItemBrand.Pioneer.value, 2050, 17)
    microphone = Microphone("Rg.pro", ItemBrand.Sim.value, 1700, 25)

    manager = Manager()
    manager.items_brand = [lamp, camera, microphone]
    manager.print_list(manager.items_brand)
    manager.items_brand = manager.sort_by_price()
    manager.print_list(manager.items_brand)
    manager.items_brand = manager.find_by_item_brand("LG")
    manager.print_list(manager.items_brand)
