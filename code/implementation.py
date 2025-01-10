from dataset import DataSetInterface, DataSetItem

class DataSet(DataSetInterface):
    def __init__(self, items=None):
        super().__init__()
        self.data = {}
        if items:
            for item in items:
                self += item

    def __setitem__(self, name, id_content):
        id, content = id_content
        self.data[name] = DataSetItem(name, id, content)

    def __iadd__(self, item):
        self.data[item.name] = item
        return self

    def __delitem__(self, name):
        if name in self.data:
            del self.data[name]

    def __contains__(self, name):
        return name in self.data

    def __getitem__(self, name):
        return self.data[name]

    def __and__(self, dataset):
        common_keys = self.data.keys() & dataset.data.keys()
        return DataSet([self.data[key] for key in common_keys])

    def __or__(self, dataset):
        combined = {**self.data, **dataset.data}
        return DataSet(combined.values())

    def __iter__(self):
        items = list(self.data.values())
        if self.iterate_sorted:
            key = lambda item: item.name if self.iterate_key == self.ITERATE_SORT_BY_NAME else item.id
            items.sort(key=key, reverse=self.iterate_reversed)
        return iter(items)

    def filtered_iterate(self, filter_func):
        filtered_items = []
        for item in self.data.values():
            if filter_func(item.name, item.id):
                filtered_items.append(item)
        if self.iterate_sorted:
            key = lambda item: item.name if self.iterate_key == self.ITERATE_SORT_BY_NAME else item.id
            filtered_items.sort(key=key, reverse=self.iterate_reversed)
        return iter(filtered_items)

    def __len__(self):
        return len(self.data)
