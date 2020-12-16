import flask
from requests import get
from rockset import Client, ParamDict, Q, F
from os import getenv

rs = Client(api_key=getenv('ROCKSET_SECRET'), api_server='api.rs2.usw2.rockset.com')

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def null():
    return('<script>location.replace("http://github.com/gadhagod/Heroku-Status-Badges")</script>')

@app.route('/<app_name>', methods=['GET'])
def running(app_name):
    code = get('https://{}.herokuapp.com/'.format(app_name)).status_code
    if code >= 500 and code <= 599:
        return(flask.send_file('badges/down.png', mimetype='image/png'))
    elif code == 404:
        return(flask.send_file('badges/not_found.png', mimetype='image/png'))
    else:
        return(flask.send_file('badges/running.png', mimetype='image/png'))