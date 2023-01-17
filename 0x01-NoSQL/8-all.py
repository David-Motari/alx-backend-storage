#!/usr/bin/env python3
"""
8-all
"""


def list_all(mongo_collection):
    """
        function that lists all documents in a collection
    """
    list_docs = list(mongo_collection.find())
    if len(list_docs) == 0:
        return []
    return list_docs

