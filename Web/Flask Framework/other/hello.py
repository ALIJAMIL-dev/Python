# A Simple Example
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Routing
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# Variable Rules
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

# Unique URLs / Redirection Behavior
# (handled by trailing slash in routes, e.g., /projects/)

# URL Building
from flask import url_for
with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('projects'))
    print(url_for('about'))

# HTTP Methods
def do_the_login():
    pass
def show_the_login_form():
    pass

from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

# Static Files
url_for('static', filename='style.css')

# Rendering Templates
from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# HTML Escaping
from markupsafe import escape
@app.route('/<name>')
def escaped(name):
    return f'Hello {escape(name)}'

# Request Object
with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

# File Uploads
from flask import request
@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['the_file']
    f.save('/path/to/save/file.txt')

# Cookies
from flask import make_response
@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Cookie Set")
    resp.set_cookie('username', 'the username')
    return resp

# Redirects and Errors
from flask import abort, redirect, url_for
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login_redirect():
    abort(401)

# Custom Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Responses
@app.route('/custom_response')
def custom_response():
    resp = make_response(render_template('index.html'))
    resp.headers['X-Something'] = 'A value'
    return resp

# Sessions
from flask import session
app.secret_key = 'super secret key'

@app.route('/set_session')
def set_session():
    session['username'] = 'admin'
    return 'Session set!'

@app.route('/get_session')
def get_session():
    return session.get('username', 'not set')

# Message Flashing
from flask import flash, get_flashed_messages
@app.route('/flash')
def flash_message():
    flash('Hello, Flask!')
    return str(get_flashed_messages())

# Logging
app.logger.debug('A debug message')
app.logger.warning('A warning')
app.logger.error('An error occurred')

# Hooking in WSGI
def application(environ, start_response):
    response_body = b'Hello World'
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

# Run the App
if __name__ == "__main__":
    app.run(debug=True)