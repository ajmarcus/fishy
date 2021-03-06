from os import getenv
from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

db = create_engine(getenv('DB'))
load = getenv('LOAD')


@app.route('/health')
def health():
    return 'healthy!'


@app.route('/{load}.txt'.format(load=load))
def load_test():
    return load


@app.route('/')
def hello_world():
    with db.connect() as c:
        result = c.execute('select message from fishy where id=1;')
        return result.fetchone()['message']
