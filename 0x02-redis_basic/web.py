#!/usr/bin/env python3
"""Redis Basics"""
import requests
from functools import wraps
from typing import Callable
import uuid
import redis

redis = redis.Redis()


def cache_count(method: Callable) -> Callable:
    """
    Add counting and caching functionality to method
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """Addds functionailty to method"""
        cache_key: str = args[0]
        if redis.get(cache_key):
            return redis.get(cache_key).decode('utf-8')

        result = method(args[0])
        redis.set(cache_key, str(result), 10)
        return method(*args, **kwargs)
    return wrapper


@cache_count
def get_page(url: str) -> str:
    """
    makes a request to the url parsed and returns
    the content in text
    """
    cache_count: str = f'count:{url}'
    redis.incr(cache_count)
    return requests.get(url).text


if __name__ == '__main__':
    get_page('http://google.com')
