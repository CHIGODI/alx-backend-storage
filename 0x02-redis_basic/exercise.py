#!/usr/bin/env python3
"""
This module contains a class Cache that makes connection to redis
"""
import redis
import uuid
from typing import Optional, Callable, Any


class Cache:
    """
    Cache class to interact with Redis for storing and retrieving data.
    """

    def __init__(self):
        """
        Initialize the Cache class.
        Establishes a connection to the Redis server and clears the
        current database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """
        Method that takes a data argument and returns a string.
        This method generate a random key (using uuid),
        store the input data in Redis using the random key and
        return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Any]] = None)\
            -> Optional[Any]:
        """
        Retrieve data from Redis using the provided key.

        :param key: The key to retrieve data from Redis.
        :param fn: Optional callable to convert the retrieved data.
        :return: The converted data if fn is provided and data exists,
                else the raw data from Redis (bytes).
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data
