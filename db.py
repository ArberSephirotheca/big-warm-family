import pymongo
import sys
if len(sys.argv) != 3:
    print("specify address and port")
    sys.exit()
    
host = sys.argv[1]
port = int(sys.argv[2])
client = pymongo.MongoClient(host= host, port = port)
print(client)
print("connect to mongodb successfully")

class db():
    def __init__(self, client):
        self.db = client["big_warm_family"]
    
    def insert_comments_info(self, comments):
        col = self.db["comments"]
        for key in comments:
            col.insert({
                "name" : key,
                "comment" : comments[key]
            })
    
    def find_comments_info(self, user_name):
        col = self.db["comments"]
        found_comments = []
        for comment in col.find({"name" : user_name}):
            found_comments.append(comment)
        return found_comments