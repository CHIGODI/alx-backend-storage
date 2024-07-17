#!/usr/bin/env python3
"""
This module contains a class Cache that makes connection to redis
"""
import redis
import uuid
from typing import Optional, Callable, Union


class Cache:
    """
    Cache class to interact with Redis for storing and retrieving data.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache class.
        Establishes a connection to the Redis server and clears the
        current database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """
        Method that takes a data argument and returns a string.
        This method generate a random key (using uuid),
        store the input data in Redis using the random key and
        return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, int, bytes, float]:
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
        return fn(data) if fn else data

    def get_str(self, key) -> Optional[str]:
        """
        Retrieve string data from Redis using the provided key.

        :param key: The key to retrieve string data from Redis.
        :return: The string data retrieved from Redis, or None
        if key doesn't exist.
        """
        return self.get(key, fn=lambda data: data.decode('utf-8'))

    def get_int(self, key) -> Optional[int]:
        """
        Retrieve integer data from Redis using the provided key.

        :param key: The key to retrieve integer data from Redis.
        :return: The integer data retrieved from Redis, or None
        if key doesn't exist.
        """
        return self.get(key, fn=lambda data: int(data) if data else None)
