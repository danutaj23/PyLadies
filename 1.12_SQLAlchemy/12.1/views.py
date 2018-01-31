from flask import render_template
from main import app
from models import BlogPosts


@app.route('/', methods=['GET', 'POST'])
def info():
    blogposts = BlogPosts.query.all()
    return render_template('info.html', blogposts=blogposts)
