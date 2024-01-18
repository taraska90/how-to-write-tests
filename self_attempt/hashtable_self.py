BLANK = object()

class HashTable:
    def __init__(self, capacity):
        self.values = [BLANK] * capacity
        self.pairs = named

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        self.values[self._index(key)] = value

    def __getitem__(self, key):
        value = self.values[self._index(key)]
        if value is BLANK:
            raise KeyError(key)
        return value


    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key):
        if key in self:
            self[key] = BLANK
        else:
            raise KeyError(key)

    def _index(self, item):
        """

        :param item: could be key or value
        :return: index hash for item
        """
        return hash(item) % len(self)