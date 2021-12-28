from flask import Flask, request
from crawler.comment import comment_crawler

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/comments')
    def comments():
        avid = request.args['avid']
        comments = comment_crawler.get_comments_info(avid)
        return '{}'.format(comments)

    app.run(host='0.0.0.0', port=5001)