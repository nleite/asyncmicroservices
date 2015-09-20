from app import db, fts


class FTSModel(object):

    def __init__(self):
        self.coll = db[fts]
        self.coll.create_index([('title', 'text')])

    def search(self, terms):
        return self.coll.find({"$text": {"$search": terms}})

class RecommsModel(object):
    @staticmethod
    def recommend_pipeline():
        return [
            {"$match":
                { "score": {"$gt": 50}}
            },
            {"$project": {
                "num_comments": 1,
                "title": 1,
                "permalink":1,
                "score": {
                    "$divide": ["$score", 10]
                    },
                "upsanddowns": {
                    "$subtract": ["$downs", "$ups"]
                    },
                }
            },
            {"$sort":{
                "upsanddowns": 1,
                "num_comments": -1,
                }
            },
            {"$limit": 12},
        ]

    def __init__(self):
        self.coll = db[fts]

    def recommend(self):
        cur = self.coll.aggregate( self.recommend_pipeline() )

        if isinstance(cur, dict):
            return cur['results']


        return cur
