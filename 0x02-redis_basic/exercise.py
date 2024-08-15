#!/usr/bin/env python3
"""
This module contains a Cache class
"""

import redis
from typing import Union, Optional, Callable
import uuid

UnionTypes = Union[str, bytes, int, float]


class Cache:
    """
    This class stores an instance of the Redis client as a private variabele
    """

    def __init__(self):
        """
        This is the initialization method for the class Cache.

        Creates a Redis client and flushes the database to ensure it is empty.
        """
        self._redis = redis.Redis()
        # Flush the Redis database to ensure that it is empty.
        self._redis.flushdb()

    def store(self, data: UnionTypes) -> str:
        """
        Store the data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key generated for the data.
        """
        key = str(uuid.uuid4())

        # Use the Redis client to set the value of the key in the database.
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> UnionTypes:
        """
        Retrieves a value from the Redis database by key.

        Args:
            key (str): The key to retrieve the value for.
            fn (Optional[Callable], optional): An optional function to apply to the retrieved value. Defaults to None.

        Returns:
            UnionTypes: The retrieved value, or the result of applying the function to the value if a function was provided.
        """
        value = self._redis.get(key)
        if fn is not None:
            return fn(value)
        return value
