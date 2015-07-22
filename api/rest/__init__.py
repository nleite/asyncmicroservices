#!/usr/bin/python
#-*- coding: utf-8 -*-
from eve import Eve

my_settings = {
    "X_DOMAINS" : '*' ,
    "MONGO_HOST": "192.168.59.103",
    "MONGO_PORT": 32051,
    "MONGO_DBNAME": "reddit",
    "DOMAIN":{"data": {}}
}

app = Eve(settings=my_settings)
