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
    
    def create_video_index(self):
        col = self.db["videos"]
        col.create_index([("avid", pymongo.ASCENDING)])

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
    
    def insert_videos_info(self, videos):
        col = self.db["videos"]
        for avid in videos:
            col.insert_one({
                'avid' : avid,
                'title' : videos[avid]['title'],
                'pic' : videos['avid']['pic'],
                'vup_name' : videos['avid']['vup_name'],
                'pubdate' : videos['avid']['pubdate'],
                'keywords' : videos['avid']['keywords']
            })
    
    def insert_vup_info(self, vups):
        col = self.db["vups"]
        for vup in vups:
            col.insert_one({
                'uid' : vup['uid'],
                'name': vup['name'],
                'avatar' : vup['avatar'],
                'space' : vup['space']
            })

    def find_comments_by_uname(self, user_name):
        col = self.db['comments']
        found_comments = []
        for comment in col.find({'uname' : user_name}):
            found_comments.append(comment)
        return found_comments
    
    def find_comment_by_uid(self, uid):
        col = self.db['comments']
        found_comments = []
        for comment in col.find({'uid': uid}):
            found_comments.append(comment)
        return found_comments
     
