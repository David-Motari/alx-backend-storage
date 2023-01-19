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
        """Wrapper for decorator functionality"""
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


def replay(func: Callable):
    """
    Display the history of calls of a particular function.
    """
    redis = redis.Redis()
    func_name = func.__qualname__
    num = redis.get(func_name).decode("utf-8")

    print("{} was called {} times:".format(func_name, num))

    insList = redis.lrange(func_name + ":inputs", 0, -1)
    outsList = redis.lrange(func_name + ":outputs", 0, -1)

    for att, dt in zip(insList, outsList):
        attr, data = att.decode("utf-8"), dt.decode("utf-8")
        print("{}(*{}) -> {}".format(func_name, attr, data))


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

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """
        converts the data back to the desired format
        """
        val = self._redis.get(key)
        if fn:
            val = fn(val)

        return val

    def get_str(self, key: str) -> str:
        """
        converts the value from binary to string format
        """
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        converts the value from binary toint format
        """
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception:
            val = 0
        return val
