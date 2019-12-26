# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, ignore_case=False, **kwargs):
        self.unique_items = []
        self.ignore_case = ignore_case
        self.items = iter(items)

    def __next__(self):
        while True:
            item = self.items.__next__()
            compare_item = None
            if self.ignore_case and type(item) is str:
                compare_item = item.lower()
            else:
                compare_item = item
            if compare_item not in self.unique_items:
                self.unique_items.append(compare_item)
                return item

    def __iter__(self):
        return self
