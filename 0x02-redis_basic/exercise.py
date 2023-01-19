#!/usr/bin/env python3
"""
exercise
"""

import redis
from typing import Union
from uuid import uuid4, UUID


class Cache:
    """
    Cache class with method store, get, get_str, get_int
    """

    def __init__(self):
        """
        constructor - stores an instance of the Redis client as a private
        variable named _redis and flush the instance using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a
        random key and return the key.
        """
        ky = str(uuid4())
        self._redis.set(ky, data)

        return ky
