import requests
import json


comment_url = 'http://api.bilibili.com/x/v2/reply'

class comment_crawler():
    def get_comments_info(self, avid):
        replies_content  = {}
        i = 1
        while True:
            params = {
                'type' : 1,
                'oid' : avid,
                'sort' : 1,
                'nohot' : 1,
                'pn' : i
            }
            response = requests.get(url = comment_url, params= params)
            jdata = response.json()
            code = jdata['code']
            msg = jdata['message']
            data = jdata['data']
            replies = data['replies']
            if code != 0 :
                print("error code : ", code)
                print(msg)
                return replies_content
                
            if len(replies) == 0:
                print("reach end of comments")
                print(replies_content)
                return replies_content
                
            for reply in replies:
                user_name = reply['member']['uname']
                comment = reply['content']['message']
                replies_content[user_name] = comment
            i += 1