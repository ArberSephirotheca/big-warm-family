import db
from utility.comment import Comment

c = Comment()
c.get_comments_info(334001342)
family = db.Mongo("127.0.0.1", 25052)
family.connect()
family.insert_comments_info(c.comments)
comments = family.find_comments_info('东北爱乐人')
for comment in comments:
    print(comment)