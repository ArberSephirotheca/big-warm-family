import requests

video_url = 'http://api.bilibili.com/x/web-interface/view'
tag_url = 'http://api.bilibili.com/x/tag/archive/tags'

class Video():
    def __init__(self ):
        self.video = None
    
    def get_video_info(self, avid):
        video_jdata = requests.get(url= video_url, params={'avid' : avid})
        tag_jdata = requests.get(url=tag_url, params={'avid' : avid})
        video_code = video_jdata['code']
        tag_code = tag_jdata['code']

        if video_code != 0:
            message = video_jdata['message']
            print(message)
            return None
        
        if tag_code != 0:
            message = tag_jdata['message']
            print(message)
            return None
        
        tag_data = tag_jdata['data']
        tags = []
        for tag in tag_data:
            tags.append(tag['tag_name'])
        
        video_data = video_jdata['data']
        title = video_data['title']
        pic = video_data['pic']
        pubdate = video_data['pubdate']
        vup_name = video_data['owner']['name']
        self.video[avid] = { 'title' : title, 'pic': pic, 'vup_name': vup_name,'pubdate': pubdate, 'keywords': tags}
        
    def get_video(self):
        return self.video
    