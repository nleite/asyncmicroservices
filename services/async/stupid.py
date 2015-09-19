#!/usr/local/bin/python
#-*- coding: utf-8 -*-
from pymongo import MongoClient, collection

class Cache(object):

    def __init__(self, backend, dbname='cache'):
        self._backend = backend
        self._db = backend[dbname]
        self._coll = self._db.counter

    def startup(self, domain, initval=0):
        doc = { '$set': {'counter': initval}}
        q = {'domain': domain}
        self._coll.update_one(q, doc,upsert=True)

    def get(self, domain):
        q = {'domain': domain}
        f = { 'counter': 1, '_id':0}
        d = self._coll.find_one(q, f)
        return d['counter'] if d else None

    def set(self, domain, value):
        doc = { '$set': {'counter': value}}
        q = {'domain': domain}
        f = { 'counter': 1, '_id':0}
        dres = self._coll.find_one_and_update(q, doc,
                projection=f, return_document=collection.ReturnDocument.AFTER)
        return dres['counter']

    def inc(self, domain):
        doc = { '$inc': {'counter': 1}}
        q = {'domain': domain}
        f = { 'counter': 1, '_id':0}
        dres = self._coll.find_one_and_update(q, doc,
                projection=f, return_document=collection.ReturnDocument.AFTER)
        return dres['counter']









