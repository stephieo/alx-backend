#!/usr/bin/env python3
""" simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """ function to generate start and end indice"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
