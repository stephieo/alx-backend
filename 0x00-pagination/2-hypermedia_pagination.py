#!/usr/bin/env python3
""" simple pagination"""
from typing import Tuple
import csv
import math
from typing import List, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """ function to generate start and end indice"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get datat for a page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        borders = index_range(page, page_size)
        page_content = self.dataset()[borders[0]:borders[1]]
        return page_content

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[int, List[List]]]:
        """ hypermedia metadata generator"""
        total_pages = math.ceil((len(self.dataset()) + 1) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1,
            "total_pages": total_pages,
        }
