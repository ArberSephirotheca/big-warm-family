import requests

video_url = 'http://api.bilibili.com/x/web-interface/view'
class video_crawler():
    def __init__(self ) -> None:
        pass
    
    def get_video_info(self, avid):
        jdata = requests.get(url= video_url, params={'avid' : avid}, timeout= 2)
        print(jdata)
        code = jdata['code']
        

    