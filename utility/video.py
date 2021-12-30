import requests

video_url = 'http://api.bilibili.com/x/web-interface/view'
class video_crawler():
    def __init__(self, avid) -> None:
        self.avid = avid
    
    def get_video_info(self):
        jdata = requests.get(url= video_url, params={'avid' : self.avid}, timeout= 2)
        print(jdata.text)
