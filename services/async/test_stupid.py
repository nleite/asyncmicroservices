#!/usr/local/bin/python
#-*- coding: utf-8 -*-
import unittest
from stupid import Cache
from pymongo import MongoClient

class CacheTest(unittest.TestCase):

    def setUp(self):
        self.mc = MongoClient()
        self.dbname = 'stupid_test'
        self.cache = Cache(self.mc, self.dbname)

    def tearDown(self):
        self.mc.drop_database(self.dbname)
        pass

    def test_startup(self):
        self.cache.startup('test')
        actual = self.mc[self.dbname].counter.find({'domain':'test'}).count()
        print actual
        assert 1 == actual

    def test_get(self):
        self.cache.startup('newdomain')
        actual = self.cache.get('newdomain')
        assert 0 == actual

    def test_get_initval(self):
        domain = 'not0domain'
        self.cache.startup(domain, 10)
        assert 10 == self.cache.get(domain)


    def test_get_nodomain(self):
        assert None == self.cache.get('nodomain')

    def test_set(self):
        domain = 'domain'
        self.cache.startup(domain)
        self.cache.set(domain, 10)

        assert 10 == self.cache.get(domain)

    def test_inc(self):
        domain = 'domain'
        self.cache.startup(domain)
        self.cache.set(domain, 10)
        self.cache.inc(domain)

        assert 11 == self.cache.get(domain)





