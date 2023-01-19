#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker
    obtain the HTML content of a particular URL and returns it """
import redis
import requests

rdis = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """
    Track how many times a particular URL was accessed in the key "count:{url}"
    and cache the result with an expiration time of 10 seconds.
    """
    rdis.set(f"cached:{url}", count)
    reqst = requests.get(url)
    rdis.incr(f"count:{url}")
    rdis.setex(f"cached:{url}", 10, rdis.get(f"cached:{url}"))
    return reqst.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
