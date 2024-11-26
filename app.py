from flask import Flask

from flask import url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'


@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'


@app.route('/test')
def test_url_for():
    return 'Test page'


if __name__ == '__main__':
    app.run()
