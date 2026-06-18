import requests

post_url = 'https://api.npoint.io/c790b4d5cab58020d391'

response = requests.get(post_url)
posts = response.json()

all_posts = []

class Post:
    def __init__(self, post):
        self.id = post['id']
        self.title = post['title']
        self.subtitle = post['subtitle']
        self.body = post['body']

for post in posts:
    post_obj = Post(post)
    all_posts.append(post_obj)
