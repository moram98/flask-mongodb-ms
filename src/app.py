from flask import Flask
from pymongo import MongoClient
from config import config

app = Flask(__name__)
client = MongoClient(config['MONGO_URI'])

@app.route('/')
def index():
    return "<h1>Hola, bienvenidos al curso del ciclo 4a</h1>"


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()