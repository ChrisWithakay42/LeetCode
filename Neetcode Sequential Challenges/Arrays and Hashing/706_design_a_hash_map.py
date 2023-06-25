class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.bucket_array = [None] * self.size

    def _get_hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_value = self._get_hash(key)
        if self.bucket_array[hash_value] is None:
            self.bucket_array[hash_value] = ListNode(key, value)
        else:
            curr = self.bucket_array[hash_value]
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                if curr.next is None:
                    break
                curr = curr.next
            curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        ...

    def remove(self, key: int) -> None:
        ...
