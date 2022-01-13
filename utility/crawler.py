import requests

user_posts_url = 'http://api.bilibili.com/x/space/arc/search'

class Crawl():
    def __init__(self):
        self.vups = []
        self.vlists = {}
    
    def add_vup(self, uid):
        self.vups.append(uid)

    def crawl_all_vlists(self):
        for uid in self.vups:
            pn = 1
            while True:
                response = requests.get(url=user_posts_url, params={'mid': uid, 'pn': pn, 'ps': 10})
                code = response['code']

                if code != 0:
                    print("error code %d", code)
                    message = response['message']
                    print(message)
                    return self.vlists

                data = response['data']
                vlist = data['list']['vlist']

                if len(vlist) == 0:
                    print("reach end of video lists")
                    return
                
                for video in vlist:
                    aid = video['aid']
                    self.vlists[uid].append(aid)             
                    
    def crawl_one_vlists(self, uid):
        pn = 1
        while True:
                response = requests.get(url=user_posts_url, params={'mid': uid, 'pn': pn, 'ps': 10})
                code = response['code']

                if code != 0:
                    print("error code %d", code)
                    message = response['message']
                    print(message)
                    return self.vlists[uid]

                data = response['data']
                vlist = data['list']['vlist']

                if len(vlist) == 0:
                    print("reach end of video lists")
                    return

                for video in vlist:
                    aid = video['aid']
                    self.vlists[uid].append(aid)
                
                pn += 1
                    
    def get_all_vlists(self):
        return self.vlists
    
    def get_one_vlist(self, uid):
        return self.vlists[uid]