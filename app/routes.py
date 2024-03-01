from app import app

@app.route('/')
def home():
    return 'My primera APP'

@app.route('/index')
def index():
    return 'This is the index route.'