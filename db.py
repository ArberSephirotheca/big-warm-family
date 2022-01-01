import pymongo

class Mongo():
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def connect(self):
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.client['big_warm_family']

    def create_comment_index(self):
        col = self.db["comments"]
        col.create_index([("uid", pymongo.ASCENDING),("date", pymongo.DESCENDING)])

    def insert_comments_info(self, comments):
        col = self.db["comments"]
        for key in comments:
            col.insert_one({
                'uid' : key,
                'uname' : comments[key]['uname'],
                'avid' : comments[key]['avid'],
                'comment' : comments[key]['comment'],
                'like' : comments[key]['like'],
                'date': comments[key]['date']
            })
    
    def find_comments_info(self, user_name):
        col = self.db['comments']
        found_comments = []
        for comment in col.find({'uname' : user_name}):
            found_comments.append(comment)
        return found_comments