#!/usr/bin/env python3
"""Redis Basics"""
import requests
from functools import wraps
from typing import Callable
import uuid
import redis

redis = redis.Redis()


def cache_count(method: Callable):
    @wraps(method)
    def wrapper(*args, **kwargs):
        """Addds functionailty to method"""
        cache_key = args[0]
        cache_count = f'count:{args[0]}'
        redis.incr(cache_count)

        if redis.get(cache_key):
            return redis.get(cache_key).decode('utf-8')

        result = method(args[0])
        redis.set(cache_key, result, 10)
        return method(*args, **kwargs)
    return wrapper


@cache_count
def get_page(url: str) -> str:
    """
    makes a request to the url parsed and returns
    the content in text
    """
    res = requests.get(url)
    return res.text


if __name__ == '__main__':
    get_page('https://www.youtube.com')
