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
    rdis.set("cached:{}".format(url), num)
    reqst = requests.get(url)
    rdis.incr("num:{}".format(url))
    rdis.setex("cached:{}".format(url), 10, r.get("cached:{}".format(url)))

    return reqst.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
