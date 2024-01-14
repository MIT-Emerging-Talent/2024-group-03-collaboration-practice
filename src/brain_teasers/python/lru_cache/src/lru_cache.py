from collections import OrderedDict


class LRUCache:
    """
    This class represents a basic LRU (Least Recently Used) cache data structure.
    It is implemented using Python's built-in OrderedDict which maintains the order of insertion of keys.
    """

    def __init__(self, capacity: int = 5):
        """
        Initializes the LRUCache object.

        :param capacity: The total size or capacity of the LRU cache.
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Retrieves an item from the cache using its key.
        The function also maintains the LRU property by moving the accessed key to the end of the cache.
        If the key is not found in the cache, the function returns -1.

        :param key: The key of the item to be retrieved from the cache.
        :type key: int
        :return: The value of the key from the cache if exist, -1 otherwise.
        :rtype: int
        """
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Inserts a key-value pair into the cache.
        If the key already exists in the cache, it updates the value and moves the key to the end of the cache to preserve the LRU property.
        If the cache is at capacity, it removes the least recently used item before inserting the new item.

        :param key: The key of the item to be inserted or updated in the cache.
        :type key: int
        :param value: The value to be associated with the key in the cache.
        :type value: int
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
