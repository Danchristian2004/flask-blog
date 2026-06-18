from flask import Flask, render_template
from post import all_posts

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None

    for post in all_posts:
        if post.id == index:
            requested_post = post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)