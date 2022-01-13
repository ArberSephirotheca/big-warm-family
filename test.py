import utility.db as db
from utility.comment import Comment
from utility.video import Video
from utility.crawler import Crawl

''''
c = Comment()
c.get_comments_info(334001342)
v = Video()
family = db.Mongo("localhost", 27017)
family.connect()
family.create_comment_index()
family.create_video_index()
family.insert_comments_info(c.comments)
comments = family.find_comments_info('东北爱乐人')
for comment in comments:
    print(comment)
'''
c = Crawl()
c.add_vup(1663853)
c.crawl_one_vlists(1663853)
print(c.get_one_vlist(1663853))