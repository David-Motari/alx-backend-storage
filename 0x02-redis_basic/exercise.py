#!/usr/bin/env python3
"""
exercise
"""

import redis
from typing import Union, Optional, Callable
from uuid import uuid4, UUID
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ 
    Decortator for counting how many times a function
    has been called 
    """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for decorator functionality """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ 
    decorator function to store history
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        decorator function
        """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper

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
