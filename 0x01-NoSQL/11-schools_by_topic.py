#!/usr/bin/env python3
"""
This module contains a function that returns a list of schools
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic(string): topic searched for 
    """
    if mongo_collection is None:
        return []
    return mongo_collection.find({"topics": topic})