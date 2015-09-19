#!/usr/bin/python
#-*- coding: utf-8 -*-
import xmltodict
import simplejson as json
import re
from datetime import datetime

def tag_spliter(tag):
    expression = r"[\<\>]"
    #return re.search( expression, tag ).groups()
    #Don't like this too much!
    return [x for x in re.split(expression, tag) if x != '']

def parse_time(dtime):
    dateformat = "%Y-%m-%dT%H:%M:%S"
    return datetime.strptime(dtime[:-4], dateformat).isoformat()


key_mapping = {
        '@Id':{'label': 'id', 'function': unicode},
        '@Title': {'label':'title', 'function': unicode},
        '@CommentCount': { 'label': 'num_comments', 'function': int},
        '@Score':{'label': 'score', 'function': int},
        '@ViewCount':{'label': 'views', 'function': int},
        '@Body': {'label':'body', 'function': unicode},
        '@Tags': {'label':'tags', 'function': tag_spliter},
        '@CreationDate': {'label':'created_utc', 'function': parse_time},
        '@LastEditDate': {'label':'last_edit', 'function': parse_time},
        '@LastActivityDate': {'label':'last_activity', 'function': parse_time},
        '@LastEditorUserId': {'label':'last_editorid', 'function': unicode},
        }

def parse(filename, key_mapping, source):
    with open(filename) as fd:
        big = xmltodict.parse(fd.read())
        docs = []
        for d in big['posts']['row']:
            ndoc = {};
            for k, v in d.iteritems():
                if key_mapping.has_key(k):
                    ndoc[key_mapping[k]['label']] = key_mapping[k]['function'](v)
                else:
                    ndoc[k.replace('@', '')]= v
                ndoc['source'] = source

                docs.append(ndoc)

        return docs

def main(filename):
    parse(filename, key_mapping, 'stackoverflow')


if __name__ == '__main__':
    filename = 'Posts10000.xml'
    main( filename )
