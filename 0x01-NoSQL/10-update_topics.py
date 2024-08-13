#!/usr/bin/env python3
"""
This module contains a function that changes all topics of document
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a document based on the name

    Args:
        mongo_collection: pymongo collection object.
        name(string): the school name to update
        topics(list of strings): list of topics
    """
    mongo_collection.find_one_and_update(
        {"name": name},
        {"$set": {"topics": topics}},
        {"multi": True}
    )
