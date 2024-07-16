#!/usr/bin/env python3

"""
Write a Python script that provides some stats about Nginx logs
stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the
method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
(see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status

You can use this dump as data sample: dump.zip

The output of your script must be exactly the same as the example
"""

from pymongo import MongoClient


def nginx_stats():
    """ returns stats of an nginx server """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print(f'{db.count_documents({})} logs')
    print(f'Methods:')

    for method in methods:
        stat = db.count_documents({'method': method})
        print(f'\tmethod {method}: {stat}')

    print(f"{db.count_documents({'method': 'GET', 'path': '/status'})}"
          f" status check")


if __name__ == '__main__':
    nginx_stats()
