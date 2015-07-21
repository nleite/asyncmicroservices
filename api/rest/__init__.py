#!/usr/bin/python
#-*- coding: utf-8 -*-
from eve import Eve

my_settings = {
    "X_DOMAINS" : '*' ,
    "MONGO_HOST": "localhost",
    "MONGO_PORT": 27017,
    "MONGO_DBNAME": "reddit",
    "DOMAIN":{"data": {}}
}

app = Eve(settings=my_settings)
