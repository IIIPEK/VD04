from flask import Flask, render_template
import json

app = Flask(__name__)

def load_json(filename='data/posts.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        posts = json.load(f)
    return posts

@app.route('/')
def index():
    home = load_json(filename='data/home.json')
    return render_template('index.html', home=home)

@app.route('/blog/')
def blog():
    posts = load_json()
    return render_template('blog.html', posts=posts)

@app.route('/contacts/')
def contacts():
    contacts = load_json(filename='data/contacts.json')
    return render_template('contacts.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)
