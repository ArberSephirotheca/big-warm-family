import requests

video_url = 'http://api.bilibili.com/x/web-interface/view'
class video_crawler():
    def __init__(self, bvid) -> None:
        self.bvid = bvid
    
    def get_video_info(self):
        jdata = requests.get(url= video_url, params={'bvid' : self.bvid}, timeout= 2)
        print(jdata.text)
