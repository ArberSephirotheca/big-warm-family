import requests

comment_url = 'http://api.bilibili.com/x/v2/reply'


class Comment():

    def __init__(self):
        self.comments = None

    def get_comments_info(self, avid):
        replies_content = {}
        i = 1
        while True:
            params = {'type': 1, 'oid': avid, 'sort': 1, 'nohot': 1, 'pn': i}
            response = requests.get(url=comment_url, params=params)
            jdata = response.json()
            code = jdata['code']
            msg = jdata['message']
            data = jdata['data']
            replies = data['replies']
            if code != 0:
                print("error code : ", code)
                print(msg)
                self.comments = replies_content
                return
            if len(replies) == 0:
                print("reach end of comments")
                self.comments = replies_content
                return
            for reply in replies:
                user_name = reply['member']['uname']
                uid = reply['mid']
                comment = reply['content']['message']
                like =  reply['like']
                date = reply['ctime']
                replies_content[uid] = {'uname':user_name, 'avid' : avid, 'comment' : comment, 'like' : like, 'date' : date}
            i += 1

    def get_users(self):
        return self.comments.keys()
    
    def get_comments(self):
        return self.comments