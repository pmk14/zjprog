from item_category import ItemCategory

class Cheese(ItemCategory):
    def update_quality(self, item):
        self.increase_quality(item)
        if item.sell_in <= 5:
            self.increase_quality(item)
        if item.sell_in <= 10:
            self.increase_quality(item)

    def update_expired(self, item):
        item.quality = 0
