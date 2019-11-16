class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def increase_quality(self):
        if self.quality < 50:
            self.quality += 1

    def decrease_quality(self):
        if self.quality > 0:
            self.quality -= 1
