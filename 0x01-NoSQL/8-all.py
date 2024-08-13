#!/usr/bin/env python3
"""
This module contains a scriot that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
        mongo_collection: pymongo collection object
    Returns:
        List of documents
    """
    if mongo_collection is None:
        return []

    return mongo_collection.find()
