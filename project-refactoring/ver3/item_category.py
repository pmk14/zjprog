class ItemCategory:
    def increase_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def decrease_quality(self, item):
        if item.quality > 0:
            item.quality -= 1

    def decrease_sell_in(self, item):
        item.sell_in -= 1

    def update_quality(self, item):
        self.decrease_quality(item)

    def update_sell_in(self, item):
        self.decrease_sell_in(item)

    def update_expired(self, item):
        self.decrease_quality(item)

    def update_item(self, item):
        self.update_quality(item)
        self.update_sell_in(item)
        if item.sell_in < 0:
            self.update_expired(item)

