#!/usr/bin/env python3
"""
This module contains a script that inserts a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insers a new document in a collection

    Args:
        mongo_collection: pymongo collection object
        kwars: keyword arguments

    Returns:
        The new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id