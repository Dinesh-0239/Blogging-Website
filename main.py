BLOG_END_POINT = 'https://api.npoint.io/f399cc5a6a73b0fd221d'

from flask import Flask, render_template
import requests

Blogs = requests.get(BLOG_END_POINT).json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs=Blogs)

@app.route('/about')
def about_():
    return render_template("about.html")

@app.route('/contact')
def contact_():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def post_(id):
    return render_template("post.html",bid=id,blogs=Blogs)

if __name__ == '__main__':
    app.run(debug=True)