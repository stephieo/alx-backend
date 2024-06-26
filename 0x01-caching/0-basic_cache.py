#!/usr/bin/env python3
""" BasicCache class """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""
    def __init__(self):
        """initialization method"""
        super().__init__()

    def put(self, key, item):
        """ add item to cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
