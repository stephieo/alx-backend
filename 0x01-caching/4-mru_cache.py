#!/usr/bin/env python3
""" LRUCache class """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU REMOVAL STRATEGY"""
    def __init__(self):
        """initialization method"""
        super().__init__()
        self.use_list = []

    def put(self, key, item):
        """add item to cache"""
        if key is None or item is None:
            return

        if key in self.use_list:
            self.use_list.remove(key)
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.use_list.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")
        self.use_list.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ return item from cache"""
        if key is None or key not in self.cache_data:
            return None
        self.use_list.remove(key)
        self.use_list.append(key)
        return self.cache_data[key]
