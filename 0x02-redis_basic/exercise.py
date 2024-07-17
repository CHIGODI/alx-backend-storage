#!/usr/bin/env python3
"""
This module contains a class Cache that makes connection to redis
"""
import redis
import uuid
from typing import Union


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

    def store(self, data: Union[int, float, bytes, str]) -> str:
        """
        Method that takes a data argument and returns a string.
        This method generate a random key (using uuid),
        store the input data in Redis using the random key and
        return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
