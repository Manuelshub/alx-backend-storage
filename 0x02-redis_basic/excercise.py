#!/usr/bin/env python3
"""
This module contains a Cache class
"""
import redis
from typing import Union
import uuid


class Cache:
    """
    This class stores an instance of the Redis client as a private variabele
    """

    def __init__(self) -> None:
        """
        This is the initialization method for the class Cache.

        It creates a Redis client and flushes the database to ensure that it is empty.
        """
        self.__redis = redis.Redis()
        # Flush the Redis database to ensure that it is empty.
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key generated for the data.
        """
        key = str(uuid.uuid4())

        # Use the Redis client to set the value of the key in the database.
        self.__redis.set(key, data)
        return key
