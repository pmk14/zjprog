from item_category import ItemCategory
from cheese import Cheese
from backstage_pass import BackstagePass
from legendary import Legendary

class GildedRose:
    @staticmethod
    def categorize(item):
        if item.name == "Aged Brie":
            return Cheese()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return Legendary()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass()
        return ItemCategory()
    
    @staticmethod
    def update_quality(items):
        for i in range(0, len(items)):
            category = GildedRose.categorize(items[i])
            category.update_item(items[i])

        return items
