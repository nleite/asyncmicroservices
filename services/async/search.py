#!/usr/local/bin/python
#-*- coding: utf-8 -*-
import tornado.escape
import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient
from pymongo import MongoClient, TEXT
from datetime import datetime
import time


class FTSHandler(tornado.web.RequestHandler):

    def initialize(self, collection):
        self._coll = collection
        self._coll.create_index([('title', TEXT)])


    def format_response(self, item):
        doc = { '_id': str(item['_id']),
                'url': item['url'],
                'permalink': item['permalink'],
                'text': item['title']}
        return doc

    def get(self, term):
        cur = self._coll.find( {"$text": {"$search": term, "$language": 'english'}})

        docs = []
        for item in cur:
            docs.append(self.format_response(item))

        self.write({'result':docs})


class SearchTermHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, term):
        print "HERE"
        AsyncHTTPClient().fetch(
                'http://localhost:8181/fts/{0}'.format(term),
                callback=self.on_response
                );

    def format_response(self, item):
        doc = { '_id': item['_id'],
                'link': '/post/{}'.format(item['_id']),
                'permalink': item['permlink'],
                }

    def on_response(self, response):

        print response
        doc_response = { 'data': [], 'count': 0}
        for item in response['result']:
            doc_response['data'].append( self.format_response(item) )
            doc_response['count'] = doc_response['count'] + 1

        self.write(doc_response)
        self.finish()


uri = "mongodb://nair.local:27017"
databasename = 'reddit'
mc = MongoClient(uri)
db = mc[databasename]

urls = [
        (r"/search/([^/]+)", SearchTermHandler),
        (r"/fts/([^/]+)", FTSHandler, dict(collection=db.posts)),
        ]
app = tornado.web.Application(urls)

if __name__ == '__main__':
    app.listen(8181)
    tornado.ioloop.IOLoop.instance().start()
