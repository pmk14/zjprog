class GildedRose:
    @staticmethod
    def decrease_quality(item):
        if item.quality > 0:
            item.quality -= 1
 
    @staticmethod
    def increase_quality(item):
        if item.quality < 50:
            item.quality += 1
    
    @staticmethod
    def update_quality(items):
        for i in range(0, len(items)):
            if "Aged Brie" != items[i].name and "Backstage passes to a TAFKAL80ETC concert" != items[i].name:
                # TODO: Improve this code.  Word.
                if "Sulfuras, Hand of Ragnaros" != items[i].name:
                        GildedRose.decrease_quality(items[i])
            else:
                GildedRose.increase_quality(items[i])
                if "Aged Brie" == items[i].name and items[i].sell_in < 6:
                    GildedRose.increase_quality(items[i])
                # Increases the Quality of the stinky cheese if it's 11 days to due date.
                if "Aged Brie" == items[i].name and items[i].sell_in < 11:
                    GildedRose.increase_quality(items[i])
                if "Backstage passes to a TAFKAL80ETC concert" == items[i].name:
                    if items[i].sell_in < 11:
                        GildedRose.increase_quality(items[i])
                    # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                    if items[i].sell_in < 6:
                        GildedRose.increase_quality(items[i])
            if "Sulfuras, Hand of Ragnaros" != items[i].name:
                items[i].sell_in = items[i].sell_in - 1
            if items[i].sell_in < 0:
                if "Aged Brie" != items[i].name:
                    if "Backstage passes to a TAFKAL80ETC concert" != items[i].name:
                        if "Sulfuras, Hand of Ragnaros" != items[i].name:
                            GildedRose.decrease_quality(items[i])
                    else:
                        # TODO: Fix this.
                        items[i].quality = 0
                else:
                    GildedRose.increase_quality(items[i])
                    if "Aged Brie" == items[i].name and items[i].sell_in <= 0:
                        items[i].quality = 0
                        # of for.
            if "Sulfuras, Hand of Ragnaros" != items[i].name and items[i].quality > 50:
                    items[i].quality = 50
        return items
