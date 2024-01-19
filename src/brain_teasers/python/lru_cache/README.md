# LRUCache

This Python package provides a basic implementation of an LRU (Least Recently Used) cache data structure. It is implemented using Python's built-in OrderedDict and maintains the order of insertion of keys.

## Usage

To use the LRUCache class in a Python program, you must first import it:

```python  
from LRUCache import LRUCache
```

You can then create an instance of the LRUCache class:

```python  
cache = LRUCache()
```

By default, the LRUCache instance has a capacity of 5. If you wish to create an instance with a different capacity, you can pass it as an argument during instantiation:

```python
cache = LRUCache(10) # creates a cache with a capacity of 10
```

The `get(key)` method retrieves an item from the cache using its key. If the key is in the cache, the method returns its corresponding value and moves the key to the end of the cache to maintain the LRU property. If the key is not in the cache, it returns -1.

Example:

```python
value = cache.get(key)
```

### put method

The `put(key, value)` method inserts a key-value pair into the cache. If the key is already in the cache, it updates the value and moves the key to the end of the cache to maintain the LRU property. If the cache is at capacity, it removes the least recently used item before inserting the new item.

Example:
```python
cache.put(key, value)
```

## Running tests

Run `main.py` in the root folder of package (current directory)