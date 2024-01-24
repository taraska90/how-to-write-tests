from typing import Any, NamedTuple

class Pair(NamedTuple):
    key: Any
    value: Any
class HashTable:
    def __init__(self, capacity):
        self._pairs = [None] * capacity

    def __len__(self):
        return len(self._pairs)

    def __setitem__(self, key, value):
        self._pairs[self._index(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self._pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value


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
            self._pairs[self._index(key)] = None
        else:
            raise KeyError(key)

    def _index(self, item):
        """

        :param item: could be key or value
        :return: index hash for item
        """
        return hash(item) % len(self)

    @property
    def pairs(self):
        return [pair for pair in self._pairs if pair]

    @property
    def values(self):
        return [pair.value for pair in self.pairs]