#!/usr/bin/env python3
"""
web
"""
import redis
import requests

rdis = redis.Redis()
num = 0


def get_page(url: str) -> str:
    """
    track how many times a particular URL was accessed in the key "count:{url}"
    and cache the result with an expiration time of 10 seconds.
    """
    rdis.set(f"cached:{url}", num)
    reqst = requests.get(url)
    rdis.incr(f"num:{url}")
    rdis.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))

    return reqst.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
