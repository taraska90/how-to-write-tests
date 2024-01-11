BLANK = object()

class HashTable:
    def __init__(self, capacity):
        self.values = [BLANK] * capacity

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        index = hash(key) % len(self)
        self.values[index] = value

    def __getitem__(self, key):
        index = hash(key) % len(self)
        value = self.values[index]
        if value is BLANK:
            raise KeyError(key)
        return value


    def __contains__(self, key):
        index = hash(key) % len(self)
        if self.values[index]:
            return key
        else:
            raise KeyError(key)
