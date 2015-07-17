from app import db, fts


class FTSModel(object):

    def __init__(self):
        self.coll = db[fts]
        self.coll.create_index([('title', 'text')])

    def search(self, terms):
        return self.coll.find({"$text": {"$search": terms}})
