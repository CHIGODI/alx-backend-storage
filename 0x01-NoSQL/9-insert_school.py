#!/usr/bin/env python3
"""
A Python function that inserts a new document in a collection
based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The collection to insert the document into.
        **kwargs: The key-value pairs representing the document to be inserted.

    Returns:
        The ID of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
