from flask import Flask, request, render_template
from utility.comment import Comment

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/comments')
    def comments():
        avid = request.args['avid']
        comment = Comment()
        comment.get_comments_info(avid)
        return render_template("index.html", comment=comment.comments)

    @app.route('/comments/users')
    def comments_users():
        avid = request.args['avid']
        comment = Comment()
        comment.get_comments_info(avid)
        return '{}'.format(comment.get_users())

    app.run(host='0.0.0.0', port=5001)