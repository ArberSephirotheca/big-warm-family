from flask import Flask, request
from utility.comment import Comment

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/comments')
    def comments():
        avid = request.args['avid']
        comment = Comment()
        comment.get_comments_info(avid)
        return '{}'.format(comment.comments)

    @app.route('/comments/users')
    def comments_users():
        avid = request.args['avid']
        comment = Comment()
        comment.get_comments_info(avid)
        return '{}'.format(comment.get_users())

    app.run(host='0.0.0.0', port=5001)