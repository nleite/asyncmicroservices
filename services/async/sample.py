#!/usr/bin/python
#-*- coding: utf-8 -*-
import tornado.escape
import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient
import time
def format_response(response):
    return { 'code': 'OK', 'count': 10}

class CounterHandler(tornado.web.RequestHandler):

    def get(self):
        print("Sync Request")
        time.sleep(2)
        self.write({'count': 2000})

class AsyncCounterHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        AsyncHTTPClient().fetch(
            "http://localhost:8181/counter",
            callback=self.on_response
            );
        print("async")

    def on_response(self, response):
        formated_response = format_response(response)
        self.write(formated_response)
        self.finish()

urls = [
        (r"/counter", CounterHandler),
        (r"/countasync", AsyncCounterHandler)]

app = tornado.web.Application(urls)

if __name__ == '__main__':
    app.listen(8181)
    tornado.ioloop.IOLoop.instance().start()



