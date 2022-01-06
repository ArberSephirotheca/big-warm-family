from flask import Flask, request, render_template
from utility.comment import Comment
from utility.db import Mongo

host = "localhost"
port = 27017
family = Mongo(host, port)
family.connect()

if __name__ == '__main__':
    app = Flask(__name__)

    # @app.route('/')
    # def home():
    #     return render_template("index.html")

    @app.route('/fetch_comments')
    def fetch_comments():
        avid = request.args['avid']
        comment = Comment()
        comment.get_comments_info(avid)
        return comment.comments

    @app.route('/fetch_comments/users')
    def fetch_comments_users():
        avid = request.args['avid']
        comment = Comment()
        comment.get_comments_info(avid)
        return '{}'.format(comment.get_users())

    @app.route('/find_comment')
    def find_comment():
        key = request.args('key')
        res = family.find_comments_info(key)
        return res

    app.run(host='0.0.0.0', port=5001)