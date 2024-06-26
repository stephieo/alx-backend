#!/usr/bin/env python3
""" FIFOCache class """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCAche definition"""
    def __init__(self):
        """initialization method"""
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """add item to cache"""
        if key is None or item is None:
            return
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.cache_list.pop(0)
            print(f"DISCARD {discarded_key}")
            del self.cache_data[discarded_key]
        self.cache_list.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ return item from cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
