class MyHashSet:

    def __init__(self):
        self._hash_set = []

    def add(self, key: int):
        if key not in self._hash_set:
            self._hash_set.append(key)

    def remove(self, key: int):
        if key in self._hash_set:
            self._hash_set.remove(key)

    def contains(self, key):
        return key in self._hash_set
