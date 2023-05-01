from flask import Blueprint

api = Blueprint('api',__name__,url_prefix='/api')

@api.route('/getdata')
def index():
    return '<h1>Welcome to api</h1>'