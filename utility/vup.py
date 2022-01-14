import requests

user_posts_url = 'http://api.bilibili.com/x/space/arc/search'
user_info_url = 'http://api.bilibili.com/x/space/acc/info'

class Crawl():
    def __init__(self):
        self.vups = {}
        self.vlists = {}
    
    def add_vup(self, uid):
        self.vups.append(uid)
        response = requests.get(url = user_info_url, params={'mid' : uid})
        content = response.json()
        code = content['code']

        if code != 0:
            print("error code %d", code)
            message = content['message']
            print(message)
            return self.vlists
        
        data = content['data']
        name = data['name']
        avatar = data['face']
        space = 'bilibili.com'+uid
        self.vlists[uid] = {'uid': uid, 'name': name, 'avatar': avatar, 'space' : space}

    def get_all_vlists(self):
        for uid in self.vups:
            pn = 1
            while True:
                response = requests.get(url=user_posts_url, params={'mid': uid, 'pn': pn, 'ps': 10})
                content = response.json()
                code = content['code']

                if code != 0:
                    print("error code %d", code)
                    message = content['message']
                    print(message)
                    return self.vlists

                data = content['data']
                vlist = data['list']['vlist']

                if len(vlist) == 0:
                    print("reach end of video lists")
                    return
                
                for video in vlist:
                    aid = video['aid']
                    self.vlists[uid].append(aid)             
                    
    def get_one_vlists(self, uid):
        if uid not in self.vups:
            print("ERROR unknown vup\n")
            return
        pn = 1
        while True:
                response = requests.get(url=user_posts_url, params={'mid': uid,'pn': pn, 'ps': 10})
                content =response.json()
                code = content['code']
                if code != 0:
                    print("error code %d", code)
                    message = content['message']
                    print(message)
                    return self.vlists[uid]

                data = content['data']
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
    
    def get_one_info(self, uid):
        return self.vups[uid]