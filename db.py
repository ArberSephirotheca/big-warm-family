import pymongo

class Mongo():
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def connect(self):
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.client['big_warm_family']

    def insert_comments_info(self, comments):
        col = self.db["comments"]
        print(col)
        for key in comments:
            col.insert_one({
                'name' : key,
                'comment' : comments[key]
            })
    
    def find_comments_info(self, user_name):
        col = self.db['comments']
        found_comments = []
        for comment in col.find_one({'name' : user_name}):
            found_comments.append(comment)
        return found_comments