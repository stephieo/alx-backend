#!/usr/bin/env python3
""" LFUCache class """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU REMOVAL STRATEGY"""
    def __init__(self):
        """initialization method"""
        super().__init__()
        self.freq_record = {}

    def put(self, key, item):
        """add item to cache"""
        if key is None or item is None:
            return

        if key in self.freq_record:
            # UPDATE COUNTER FOR NUMBER OF USES
            self.freq_record[key] += 1

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # IDENTIFY LEAST USED ITEM
            self.sorted_record = sorted(self.freq_record.items(),
                                        key=lambda freq: freq[1])
            discarded_key = self.sorted_record[0][0]
            del self.freq_record[discarded_key]
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")
        self.freq_record[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """ return item from cache"""
        if key is None or key not in self.cache_data:
            return None
        # UPDATE COUNTER FOR NUMBER OF USES
        self.freq_record[key] += 1
        return self.cache_data[key]
