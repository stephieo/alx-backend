#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Union[int, None] = None,
                        page_size: int = 10) -> Dict:
        """ returns a dictionary of info on data in current page,
        includes logic to skip deleted indices
        """

        idx_data_length = len(self.indexed_dataset())
        assert isinstance(index, int) and 0 <= index < idx_data_length
        self.data_count = 0
        next_index = index

        self.current_page_data = []

        while self.data_count < page_size and index < idx_data_length:
            if (next_index) in self.__indexed_dataset:
                self.current_page_data.append(
                                    self.__indexed_dataset[next_index])
                self.data_count += 1
            next_index += 1
        return {
            "index": index,
            "data": self.current_page_data,
            "page_size": page_size,
            "next_index": next_index if next_index < idx_data_length else None,
        }
